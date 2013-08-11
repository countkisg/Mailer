import sys
import email
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart

from smtp import SMTP

class Message(object):

    def __init__(self, from_addr=None, to_addr=None, subject=None, text_body=None, html_body=None, cc=None, bcc=None, headers=None, charset='utf-8'):
        if to_addr:
            if isinstance(to_addr, list):
                self._to = to_addr
            else:
                self._to = [to_addr]

            self._from = from_addr
            self._subject = subject
            self._body_parts = []

            if text_body:
                self._body_parts.append(('text/plain', text_body, charset))
            if html_body:
                self._body_parts.append(('text/html', text_body, charset))

            if cc:
                self._cc = cc
            else:
                self._cc = None
            if bcc:
                self._bcc = bcc
            else:
                self._bcc = None
            if headers:
                self._headers = headers
            else:
                self._headers = {}
            self._charset = charset

    def send(self, **kwargs):
        conn = SMTP(**kwargs)
        status = conn.send(self)

        return conn, status

    def _addrs_to_header(self, addrs):
        _addrs = []
        for addr in addrs:
            if not addr:
                continue
            if isinstance(addr, basestring):
                _addrs.append(addr)

        return unicode(',', self._charset).join(_addrs)

    def to_mime_message(self):
        msg = MIMEMultipart()

        msg['from'] = self._addrs_to_header([self._from]).encode(self._charset)
        msg['to'] = self._addrs_to_header(self._to).encode(self._charset)
        msg['subject'] = self._subject.encode(self._charset) or ''

        if self._cc:
            msg['cc'] = self._cc.encode(self._charset)
        if self._bcc:
            msg['bcc'] = self._bcc.encode(self._charset)

        if self._headers:
            for key, value in self._headers.iteritems():
                msg[key] = value.encode(self._charset)

        for part in self._body_parts:
            maintype, subtype = part[0].split('/')
            if maintype == 'text':
                msg.attach(MIMEText(part[1].encode(self._charset), _subtype=subtype))

        return msg

    @property
    def to_addr(self):
        return self._to

    def add_to_addr(self, to_addr):
        self._to.append(to_addr)

    def change_to_addr(self, l, to_addr):
        self._to[l] = to_addr

    @property
    def from_addr(self):
        return self._from
