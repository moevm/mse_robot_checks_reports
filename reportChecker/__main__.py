import sys, inspect, os
import json
from lib.mailagent import MailAgent
from lib.verifier import Archiver
from lib.database import DatabaseDAO
from lib.config import ConfigReader
from lib.subject import Subject
from pymongo import MongoClient

def run_project(args):
    os.chdir(os.path.dirname(__file__))

    #reading config    
    config = ConfigReader(os.path.abspath("resources/config.json"))
    config.read_configs()    

    #mail info
    address = config.get_email_address()
    password = config.get_email_password()

    #subject info from config
    groups = config.get_groups()
    discInfoList = []
    
    for group in groups:
        disciplines = config.get_disciplines_for_group(group)
        subjList = []
        for disc in disciplines:
            subject = Subject(disc.get("name"),disc.get("course_works"),disc.get("labs"), disc.get("ind_tasks"))
            subjList.append(subject)
        _tuple = (group,subjList)
        discInfoList.append(_tuple)

    #db
    dbdao = DatabaseDAO()

    #mail agent
    k = MailAgent(address,password)
    k.connect_imap()
    k.connect_smtp()
    k.get_attachments()
    mailList = k.get_list()

    for item in mailList:
        attachment = item.email_attachment
        archiver = Archiver(attachment,discInfoList)
        result = archiver.check_archive()

        #save to DB if attachment verified
        if (result == 0):
            discName = os.path.basename(attachment).split('-')[1]
            dbdao.saveDoc(item.email_sender, discName, os.path.abspath(attachment), item.email_time)
        
        resultMsg = archiver.getInfoMessage(result)

        #debug info
        print(resultMsg)

        #send email
        k.answer_to_id_email(item.email_id, resultMsg, "Результат проверки")

    print('All done')

if __name__ == '__main__':
    run_project(sys.argv)