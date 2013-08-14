from nose import tools
from imap import IMAP

class TestIMAP:

    def __init__(self):
        self._host = 'YOUR_SERVER'
        self._port = 'PORT'
        self._username = 'USERNAME'
        self._password = 'PASSWORD'

    def test_init(self):
        c = IMAP(host=self._host, port=self._port, username=self._username, password=self._password)

        tools.eq_(c._host, self._host)
        tools.eq_(c._port, self._port)
        tools.eq_(c._username, self._username)
        tools.eq_(c._password, self._password)

    def test_connect(self):
        c = IMAP(host=self._host, port=self._port, username=self._username, password=self._password)

        c.connect()
        tools.ok_(c._conn!= None)
