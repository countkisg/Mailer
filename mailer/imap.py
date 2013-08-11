import imaplib

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

    def connect(self):
        try:
            self._imap = imaplib.IMAP4_SSL(self._host, self._port)
        except:
            print "Connect error"
        try:
            self._login = self._imap.login(self._username, self._password)
            if self._login[0] == 'OK':
                self._is_login = True
        except:
            print "Login error ,please check username and password"
