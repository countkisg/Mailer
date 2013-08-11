from nose import tools
from smtp import SMTP

class TestSMTP:

    def test_initilize(self):
        c = SMTP(host='YOUR_SERVER', port=587, username='YOUR_USERNAME', password='YOUR_PASSWORD', ssl=True)

        tools.eq_(c._host, 'YOUR_SERVER')
        tools.eq_(c._port, 587)
        tools.eq_(c._username, 'YOUR_USERNAME')
        tools.eq_(c._password, 'YOUR_PASSWORD')
        tools.eq_(c._ssl, True)

    def test_connect(self):
        c = SMTP(host='YOUR_SERVER')
        c.connect()

        tools.ok_(c._conn != None)

        old_conn = c._conn
        c.connect()

        tools.eq_(c._conn, old_conn)

    def test_re_connect(self):
        c = SMTP(host='YOUR_SERVER')
        c.connect()

        old_conn = c._conn

        c.connect(re_conn=True)
        tools.ok_(old_conn != c._conn)

    def test_login(self):
        c = SMTP(host='YOUR_SERVER', username='YOUR_USERNAME', password='YOUR_PASSWORD')
        c.connect()
        c.login()

        tools.ok_(c._login != None)

        old_login = c._login
        c.login()

        tools.eq_(c._login, old_login)

    def test_re_login(self):
        c = SMTP(host='YOUR_SERVER', username='YOUR_USERNAME', password='YOUR_PASSWORD')
        c.connect()
        c.login()

        old_login = c._login
        c.login(re_login=True)

        tools.ok_(c._login, old_login)

    def test_is_connected(self):
        c = SMTP('YOUR_SERVER')
        c.connect()

        tools.eq_(c.is_conn, True)

    def test_send_mail(self):
        pass
