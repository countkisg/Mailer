import imaplib
from utf import *
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
        # attribute  _boxnames is coded by unicode
        # No matter what the $LANG is in your computer ,you can use "print  self._boxnames"
        #    to  output chinese characters .Also unicode characters can be converted format conveniently.
        self._boxnames = []
        
    def connect(self):
        try:
            self._imap = imaplib.IMAP4_SSL(self._host, self._port)
        except:
            print "Connect error"
        try:
            self._login = self._imap.login(self._username, self._password)
            if self._login[0] == 'OK':
                self._is_login = True
            else:
                print 'login error'
        except:
            print "Login error ,please check username and password"

    def getboxnames(self):
        if self._is_login:
            try:
                response , mailbox_list = self._imap.list()
                if response == 'OK':
                    for mailbox in mailbox_list:
                        boxname_utf7 = mailbox.split('"/"')[-1].replace('"','').strip()
                        boxname = decoder(boxname_utf7)
                        #print boxname.encode('utf-8')
                        self._boxnames.append(boxname)
            except:
                print "error while trying to use list() "



