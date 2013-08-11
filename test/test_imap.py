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

