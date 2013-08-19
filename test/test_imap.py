# -*- coding=utf8 -*-
from nose import tools
from imap import IMAP 
import time
class TestIMAP:
    def __init__(self):
        self._host = 'imap.163.com'
        self._port = 993
        self._password = 'debug123'
        self._username = 'debugmailpy@163.com'
    def test_init(self): 
        c=IMAP(host=self._host, port=self._port, username=self._username, password=self._password)

        tools.eq_(c._host, self._host)
        tools.eq_(c._port, self._port)
        tools.eq_(c._username,self._username)
        tools.eq_(c._password, self._password)
        
    def test_connect(self):
        c = IMAP(host=self._host, port=self._port, username=self._username, password=self._password)

        c.connect()
        tools.ok_(c._imap != None)
        c.closeall()
    def test_get_boxnames(self):
        c  = IMAP(host=self._host, port=self._port, username=self._username, password=self._password)
        c.connect()

        c.get_boxnames()
        tools.eq_(c._boxnames[0], 'INBOX')
        tools.eq_(c._boxnames[1], '草稿箱')
        tools.eq_(c._boxnames[2], '已发送')
        tools.eq_(c._boxnames[3], '已删除')
        tools.eq_(c._boxnames[4], '垃圾邮件')
        tools.eq_(c._boxnames[5], '病毒文件夹')
        c.closeall()
    def test_get_mails(self):
        c = IMAP(host=self._host, port=self._port, username=self._username, password=self._password)
        c.connect()
        emails = c.get_mails('INBOX',1,20)
        tools.ok_(emails !=None)
        emails = c.get_mails('INBOX', -1,-22)
        tools.ok_(emails != None)
        emails = c.get_mails('sss' , 1, 20)
        tools.ok_(emails[0] == 'NO')
        c.closeall()
    def test_check_recent(self):
        
        c = IMAP(host=self._host, port=self._port, username=self._username, password=self._password)
        c.connect()
        num = c.check_recent()[-1]
        tools.ok_(num == 0)
        #
        #send one new mail to test mail address
        #
        time.sleep(10)
        num =c.check_recent()[-1]
        tools.ok_(num == 1)

        c.closeall()

    def test_get_mails(self):

        c = IMAP(host=self._host, port=self._port, username=self._username, password=self._password)
        c.connect()
        mail = c.get_recent()
        tools.ok_(len(mail) == 1)
        mail = c.get_recent()
        tools.ok_(len(mail) == 0)
        c.closeall()
