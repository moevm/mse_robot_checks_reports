"""Work with mail"""
from imaplib import IMAP4_SSL
import sys
import imaplib
import getpass
import email
import email.header
import datetime
import os
import smtplib
from email.mime.text import MIMEText

YA_HOST = "imap.yandex.ru"
YA_SMTP = "smtp.yandex.ru"
YA_PORT = 993
YA_SMTP_PORT = 25
YA_USER = "romzhuravlev@yandex.ru"
YA_PASSWORD = "Qpwoei2209"
detach_dir = 'C:\\Users\\Roman Zhuravlev\\Downloads'

# SMTP-сервер
server = "smtp.yandex.ru"
port = 25
user_name = "romzhuravlev@yandex.ru"
user_passwd = "Qpwoei2209"

me = "romzhuravlev@yandex.ru"

s = smtplib.SMTP(server, port)
M = imaplib.IMAP4_SSL('imap.yandex.ru')


def process_mailbox(M):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
        frm = email.header.make_header(email.header.decode_header(msg['From']))
        subject = str(hdr)
        print('Message %s: %s' % (num, subject))
        print('Raw Date:', msg['Date'])
        print('From:', frm)
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print ("Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S"))


class MailAgent:
    """Work with mail"""
    def __init__(self):
        pass

    def getmail(self):
        try:
            rv, data = M.login(YA_USER, YA_PASSWORD)
        except imaplib.IMAP4.error:
            print("LOGIN FAILED!!! ")
            sys.exit(1)

        print(rv, data)

        rv, mailboxes = M.list()
        if rv == 'OK':
            print("Mailboxes:")
            print(mailboxes)

        rv, data = M.select()
        if rv == 'OK':
            print("Processing mailbox...\n")
            process_mailbox(M)

        else:
            print("ERROR: Unable to open mailbox ", rv)

    def sendmail(self, reciever, text, subj):
        msg = MIMEText(text, "", "utf-8")
        msg['Subject'] = subj
        msg['From'] = me
        msg['To'] = reciever

        # отправка
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(user_name, user_passwd)
        s.sendmail(me, reciever, msg.as_string())
        s.quit()
        return True


M.close()
M.logout()