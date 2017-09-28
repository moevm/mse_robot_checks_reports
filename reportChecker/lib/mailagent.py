"""Work with mail"""
from imaplib import IMAP4_SSL

YA_HOST = "imap.yandex.ru"
YA_PORT = 993
YA_USER = "LOGIN"
YA_PASSWORD = "PASSWORD"

class MailAgent:
    """Work with mail"""
    def __init__(self):
        pass

    def getmail(self):
        mail = {}
        mail['mailname'] = 'name'
        mail['data'] = 'data'
        return mail

    def sendmail(self, reciever, text):
        return True