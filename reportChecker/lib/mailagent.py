#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Work with mail"""
from imaplib import IMAP4_SSL
import sys
import imaplib
import email
import email.header
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.header import decode_header

YA_HOST = "imap.yandex.ru"
YA_SMTP = "smtp.yandex.ru"
YA_PORT = 993
YA_SMTP_PORT = 25
YA_USER = "romzhuravlev@yandex.ru"
YA_PASSWORD = "Qpwoei2209"
detach_dir = os.getcwd()

# SMTP-сервер
server = "smtp.yandex.ru"
port = 25
user_name = "romzhuravlev@yandex.ru"
user_passwd = "Qpwoei2209"

me = "romzhuravlev@yandex.ru"

s = smtplib.SMTP(server, port)
M = imaplib.IMAP4_SSL('imap.yandex.ru')

if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

import re

# Для декодирования аттачмента
quopri_entry = re.compile(r'=\?[\w-]+\?[QB]\?[^?]+?\?=')

def decode_multiple(encoded, _pattern=quopri_entry):
    fixed = '\r\n'.join(_pattern.findall(encoded))
    output = [b.decode(c) for b, c in decode_header(fixed)]
    return ''.join(output)

#парсит адрес отправителя (отделяет сам адрес от строки где адрес и имя, так его возвращает header)
def parseFrom(sender):
    correctEmail =''
    if(type(sender) is str):
       for i in range(0, sender.__len__()):
           if sender[i] != '<':
               continue
           else:
               for j in range(i+1, sender.__len__()-1):
                   correctEmail += sender[j]
    return correctEmail


#класс предмета листа класса MailAgent, поля: УИ письма, отправитель, вложение соответсвенно
class MailItem:
    email_id = ''
    email_sender = ''
    email_attachment = ''

    def __init__(self, id, email, attach):
        self.email_id =  id
        self.email_sender = parseFrom(email)
        self.email_attachment = attach
        pass

    def getID(self):
        return self.email_id

    def getSender(self):
        return self.email_sender

    def getAttachment(self):
        return self.email_attachment


class MailAgent:
    """Work with mail"""
    __list = []

    def __init__(self):
        pass

    #подключение по imap
    def connect_imap(self):
        try:
            rv, data = M.login(YA_USER, YA_PASSWORD)
        except imaplib.IMAP4.error:
            print("LOGIN FAILED!!! ")
            sys.exit(1)

    # подключение по smtp
    def connect_smtp(self):
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(user_name, user_passwd)

    #отправить письмо по адресу reciever c текстом text и темой письма subj (требуется предварительный вызов ф-ии connect_smtp())
    def sendmail(self, reciever, text = 'Wrong report', subj = 'From moevm (report error)'):
        msg = MIMEText(text, "", "utf-8")
        msg['Subject'] = subj
        msg['From'] = me
        msg['To'] = reciever

        s.sendmail(me, reciever, msg.as_string())
        return True

    #получает вложения ВСЕХ писем (можно изменить на входящие изменив ALL на INBOX)
    #и заносит вложения в __list класса MailAgent
    def get_attachments(self):
        rv, mailboxes = M.list()
        if rv == 'OK':
            print("List loaded.\n")
        rv, data = M.select()
        if rv == 'OK':
            print("Mailbox selected.\n")

        rv, data = M.search(None, "ALL")
        attachMass = []
        filePath =''
        for msgId in data[0].split():
            typ, messageParts = M.fetch(msgId, '(RFC822)')
            if typ != 'OK':
                print('Error fetching mail.')
                raise

            emailBody = messageParts[0][1]
            mail = email.message_from_bytes(emailBody)
            frm = email.header.make_header(email.header.decode_header(mail['From']))
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    # print part.as_string()
                    continue
                if part.get('Content-Disposition') is None:
                    # print part.as_string()
                    continue
                fileName = part.get_filename()
                # fileName = str(decode_header(fileName)[0][0])
                # fileName = fileName[2:-1]
                fileName = decode_multiple(fileName)
                if bool(fileName) and type(fileName) is str:
                    filePath = os.path.join(detach_dir, 'attachments', fileName)
                    filePath = str(decode_header(filePath)[0][0])
                    filePath.encode('utf-8')
                    if not os.path.isfile(filePath):
                        print(filePath)
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
            print(str(msgId) + " and  " + str(frm))
            item = MailItem(str(msgId), str(frm), filePath)
            self.append_to_list(item)

    #добавляет в лист
    def append_to_list(self, item):
        self.__list.append(item)

    def get_list(self):
        return self.__list
    #ниже id - это идентификатор письма ( формат : b'{номер письма}')
    def get_sender_by_id(self, id):
        for it in self.__list:
            if it.getID() == id:
                return it.getSender()

    def get_attachment_by_id(self, id):
        for it in self.__list:
            if it.getID() == id:
                return it.getAttachment()
    #ответить на письмо с идентификатором id
    def answer_to_id_email(self, id, text, subj):
        for it in self.__list:
            if it.getID() == id:
                self.sendmail(it.getSender(), text, subj)

# #выполняемый код
# k = MailAgent()
# k.connect_imap()
# k.connect_smtp()
# #k.getmail()
# k.get_attachments()
# print("TEST AREA!!!!")

# mailList = k.get_list()
# for item in mailList:
#     attachment = item.email_attachment
#     print(attachment)
#     k.answer_to_id_email(item.email_id, "nice one", "Answer")

# # t = k.get_attachment_by_id("b'3'")
# # print(t)

# # k.answer_to_id_email("b'4'", "LOOOOOOOOOOOOL", "TEST1")
# # k.answer_to_id_email("b'4'", "LOOOOOOOOOOOOL", "TEST2")
# # k.answer_to_id_email("b'4'", "LOOOOOOOOOOOOL", "TEST3")

# M.logout()
