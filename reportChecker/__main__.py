import sys, inspect, os

#sys.path.append(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

from lib.mailagent import MailAgent
from lib.verifier import Verifier
from lib.database import DatabaseDAO
from pymongo import MongoClient

def run_project(args):
    
    mailagent = MailAgent()
    mailagent.connect_imap()
    mailagent.getmail()
    attachments = mailagent.getAttachments()
    
    dbdao = DatabaseDAO()

    for attach in attachments:
        verif = Verifier(attach)
        print("ATTACH: " + attach)
        result = verif.verifydata()
        print(result)
        if result == "Файл принят.":
            dbdao.saveDoc('sender','discipline',os.path.abspath(attach))

    cclient = MongoClient()
    cdb = cclient.verificated_docs
    ccollection = cdb.docs

    print(ccollection.find())
    print(ccollection.find().count())
    for doc in ccollection.find():
        print(doc)    

    # mail = mailagent.getmail()
    # sender = 'sender from mail'
    # result = verif.verifymail(mail)

    # if not(result[0]):
    #     mail.sendmail(sender,result[1])
    # else:
    #     pass #somedb work

    print('All done')

if __name__ == '__main__':
    run_project(sys.argv)