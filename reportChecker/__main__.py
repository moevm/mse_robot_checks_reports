import sys, inspect, os
import json

#sys.path.append(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

from lib.mailagent import MailAgent
from lib.archiver import Archiver
from lib.database import DatabaseDAO
from lib.config import ConfigReader
from lib.subject import Subject
from pymongo import MongoClient

def run_project(args):
    os.chdir(os.path.dirname(__file__))
    print(os.getcwd())

    #reading config    
    config = ConfigReader(os.path.abspath("resources/config.json"))
    json_string = config.read_configs()    
    jsonObj = json.loads(json_string)

    #debug info:
    print(json_string)

    #subject info from config
    subjects_list = []
    for disc in jsonObj.get("disciplines"):
        disciplineToAdd = Subject(disc.get("name"), \
            disc.get("course_works"), disc.get("labs"),\
            disc.get("ind_tasks"))
        subjects_list.append(disciplineToAdd)       

    #db
    dbdao = DatabaseDAO()

    #mail agent
    k = MailAgent()
    k.connect_imap()
    k.connect_smtp()
    k.get_attachments()

    mailList = k.get_list()
    for item in mailList:
        attachment = item.email_attachment

        #debug info
        print(attachment)

        archiver = Archiver(attachment,subjects_list)
        result = archiver.check_archive()

        #debug info
        print(result)

        #save to DB if attachment verified
        if (result == 0):
            discName = os.path.basename(attachment).split('-')[1]
            dbdao.saveDoc(item.email_sender, discName, os.path.abspath(attachment))
        
        resultMsg = archiver.getInfoMessage(result)

        #debug info
        print(resultMsg)

        #send email
        k.answer_to_id_email(item.email_id, resultMsg, "Результат проверки")

    #debug info - print db items
    # cclient = MongoClient()
    # cdb = cclient.verificated_docs
    # ccollection = cdb.docs

    # print(ccollection.find())
    # print(ccollection.find().count())
    # for doc in ccollection.find():
    #     print(doc)    

    print('All done')

if __name__ == '__main__':
    run_project(sys.argv)