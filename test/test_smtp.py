from nose import tools
from smtp import SMTP

class TestSMTP:

    def __init__(self):
        self._host = 'YOUR_SERVER'
        self._port = 'PORT'
        self._username = 'USERNAME'
        self._password = 'PASSWORD'
        self._ssl = True

    def test_initilize(self):
        c = SMTP(host=self._host, port=self._port, username=self._username, password=self._password, ssl=True)

        tools.eq_(c._host, self._host)
        tools.eq_(c._port, self._port)
        tools.eq_(c._username, self._username)
        tools.eq_(c._password, self._password)
        tools.eq_(c._ssl, self._ssl)

    def test_connect(self):
        c = SMTP(host=self._host)
        c.connect()

        tools.ok_(c._conn != None)

        old_conn = c._conn
        c.connect()

        tools.eq_(c._conn, old_conn)

    def test_re_connect(self):
        c = SMTP(host=self._host)
        c.connect()

        old_conn = c._conn

        c.connect(re_conn=True)
        tools.ok_(old_conn != c._conn)

    def test_login(self):
        c = SMTP(host=self._host, username=self._username, password=self._password)
        c.connect()
        c.login()

        tools.ok_(c._login != None)

        old_login = c._login
        c.login()

        tools.eq_(c._login, old_login)

    def test_re_login(self):
        c = SMTP(host=self._host, username=self._username, password=self._password)
        c.connect()
        c.login()

        old_login = c._login
        c.login(re_login=True)

        tools.ok_(c._login, old_login)

    def test_is_connected(self):
        c = SMTP(self._host)
        c.connect()

        tools.eq_(c.is_conn, True)

    def test_send_mail(self):
        pass
