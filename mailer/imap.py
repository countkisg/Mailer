import sys , traceback
import email
import imaplib
from utf import *
import re

class IMAP(object):

    def __init__(self, host, port = 993, username=None, password=None):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._login = None
        self._imap = None
        self._mailbox = None
        self._is_login = False
        # attribute  _boxnames is coded by utf-8
        # No matter what the $LANG is in your computer ,you can use "print  self._boxnames"
        #    to  output chinese characters .Also utf-8 characters can be converted format conveniently.
        self._boxnames = []
        self._boxnameToUtf7 = {}
        self._currentmailbox = None  
    def connect(self):
        try:
            self._imap = imaplib.IMAP4_SSL(self._host, self._port)
        except:
            return  ['NO' , 'Connect error']
        try:
            self._login = self._imap.login(self._username, self._password)
            if self._login[0] == 'OK':
                self._is_login = True
            else:
                return['NO', 'Login error ,check username and password']
            return ['Ok','Log in ']
        except:
            return ['NO','Login error , login except']

    def get_boxnames(self):
        if self._is_login:
            try:
                response , mailboxs = self._imap.list()
                if response == 'OK':
                    for mailbox in mailboxs:
                        boxname_utf7 = mailbox.split('"/"')[-1].replace('"','').strip()
                        boxname = decoder(boxname_utf7).encode('utf-8')
                        self._boxnames.append(boxname)
                        self._boxnameToUtf7[boxname] = boxname_utf7
                return [response , response]
            except:
                trackback.print_exc()
                return ['NO' ,'Error while trying to get mailbox names ']
        else:
            return ['NO' , 'Please connect']
        
    def get_mails(self, mailbox = 'INBOX', startnum = 1 , mailnum = 20 , readonly = False):
        if self._is_login:
            if len(self._boxnameToUtf7) == 0:
                self.get_boxnames()
            if mailbox not in self._boxnameToUtf7.keys():
                return ['NO', 'Wrong mailbox name , make sure the format is UTF-8']
            try:
                snum = float(startnum)
                mnum = float(mailnum)
                startnum = int(startnum)
                mailnum = int(mnum)
            except:
                traceback.print_ext()
            try:
                emails = []
                if  self._currentmailbox :
                   self._imap.close() 
                self._imap.select(self._boxnameToUtf7[mailbox] ,True) 
                typ , num = self._imap.uid('SEARCH', None ,'All')
                if typ == 'OK':
                    allmails = len(num[0].split())
                    if mailnum < 1 or mailnum > allmails :
                        mailnum = min(20, allmails)
                    if startnum < 1 :
                        startnum = 1
                        print 'mail start number MUST be in [1 : The Number of  MAILS ]'
                    if startnum > allmails:
                        startnum = allmails - mailnum + 1
                        print 'mail start number MUST be in [1 : The Number of  MAILS ]'
                    endnum = min(startnum + mailnum -1 , allmails)                    
                    startnum = -startnum
                    endnum = -endnum - 1
                    for item in num[0].split()[startnum:endnum:-1]:
                        stat, data = self._imap.uid('FETCH', item, '(RFC822)')
                        emsg = email.message_from_string(data[0][1])
                        emails.append([item ,  emsg])
                    self._imap.close()
                if not readonly:
                    self._imap.select(self._boxnameToUtf7[mailbox],False)
                    self._currentmailbox = mailbox

                return emails
            except:
                traceback.print_exc()
                return ['NO', 'imap error' ]
        else:
            return ['NO' , 'please re-login']

    def check_recent(self, mailbox = 'INBOX'):
        if self._is_login:
            if len(self._boxnameToUtf7) == 0:
                self.get_boxnames()
            if self._currentmailbox :
                self._imap.close()
            if mailbox not in self._boxnameToUtf7.keys():
                return ['NO' , 'Wrong mailbox name , make sure the format is UTF-8']
            self._imap.select(self._boxnameToUtf7[mailbox] , True)
            typ ,num = self._imap.recent()
            self._imap.close()
            self._currentmailbox = None
            return ['OK' , int(num[0])]
        return ['NO' , 'please re-login']

    def get_recent(self, mailbox = 'INBOX'):
        if self._is_login:
            try:
                if len(self._boxnameToUtf7) == 0:
                    self.get_boxnames()
                if mailbox not in self._boxnameToUtf7.keys():
                    return ['NO' , 'Wrong mailbox name , make sure the format is UTF-8']
                if self._currentmailbox != mailbox:
                    self._imap.select(self._boxnameToUtf7[mailbox], False)
                typ , num = self._imap.uid('SEARCH', None, 'RECENT')
                emails=[]
                if typ == 'OK':
                    l = num[0].split()
                    for item in l[::-1]:
                        typ ,data = self._imap.uid('FETCH', item, '(RFC822)')
                        emsg = email.message_from_string(data[0][1])
                        emails.append([item , emsg])

                    return emails
                else:
                    return ['NO' , 'Can not get RECENT mails']
            except:
                traceback.print_exc()
                return ['NO', 'Get RECENT mails except']
        return ['NO' , 'please re-login']

    def count_mails(self , mailbox = 'INBOX'):
        if self._is_login:
            try:
                typ , num = self._imap.select(self._boxnameToUtf7[mailbox], True)
                length = num[0]
                self._imap.close()
                self._currentmailbox =None
                return length
            except:
                return ['NO' ,'get the number of selected mailbox ERROR']
        else:
            return ['NO' ,'please re-login']
    
    def closeall(self):
        if self._currentmailbox:
            self._imap.close()
        if self._imap:
            self._imap.logout()
