"""
SMTP
===============
"""

import smtplib

class SMTP(object):

    def __init__(self, host, port=465, username=None, password=None, ssl=True):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._ssl = ssl
        self._conn = None
        self._login = None

    def connect(self, re_conn=False):
        if self._conn is not None and re_conn:
            # TODO catch the exceptions
            self._conn.quit()
            self._conn = None
        elif not self._conn:
            if self._ssl:
                self._conn = smtplib.SMTP_SSL(self._host, self._port)
            else:
                self._conn = smtplib.SMTP(self._host, self._port)

    def login(self, re_login=False):
        if not self.is_conn:
            self._conn = self.connect()
        if (self._login and re_login) or not self._login:
            try:
                self._login = self._conn.login(self._username, self._password)
            except:
                print 'Fail to login'


    def send(self, message):
        if not self.is_login:
            self.login()
        #TODO formate the message and send it
        self.sendmail(message)

    def sendmail(self, message):
        f = message.from_addr
        t = message.to_addr
        msg = message.to_mime_message()
        print f, t, msg.as_string()
        # call smtp.sendmail
        return self._login.sendmail(f, t, msg.as_string())

    @property
    def is_conn(self):
        try:
            status = self._conn.noop()[0]
        except:
            status = -1

        return True if status == 250 else False
