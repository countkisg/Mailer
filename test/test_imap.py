# -*- coding=utf8 -*-
from nose import tools
from imap import IMAP 

class TestIMAP:

    def test_init(self): 
        c=IMAP(host='imap.163.com', port=993, username='debugmailpy@163.com', password='debug123')

        tools.eq_(c._host, 'imap.163.com')
        tools.eq_(c._port, 993)
        tools.eq_(c._username,'debugmailpy@163.com')
        tools.eq_(c._password, 'debug123')

    def test_connect(self):
        c = IMAP(host='imap.163.com', port=993, username='debugmailpy@163.com', password='debug123')

        c.connect()
        tools.ok_(c._imap != None)
    def test_getboxnames(self):
        c = IMAP(host='imap.163.com', port=993, username='debugmailpy@163.com', password='debug123')
        c.connect()

        c.getboxnames()
        #c._boxnames is coded by unicode and this python file is coded by utf8
        #so use u'草稿箱'  instead of '草稿箱'
        #the u before '草稿箱' means that characters is coded by unicode
        tools.eq_(c._boxnames[0], u'INBOX')
        tools.eq_(c._boxnames[1], u'草稿箱')
        tools.eq_(c._boxnames[2], u'已发送')
        tools.eq_(c._boxnames[3], u'已删除')
        tools.eq_(c._boxnames[4], u'垃圾邮件')
        tools.eq_(c._boxnames[5], u'病毒文件夹')


