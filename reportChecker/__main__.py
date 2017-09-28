import sys, inspect, os

sys.path.append(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

from lib.mailagent import MailAgent
from lib.verifier import Verifier
from lib import database

def run_project(args):
    
    mailagent = MailAgent()
    verif = Verifier()

    mail = mailagent.getmail()
    sender = 'sender from mail'
    result = verif.verifymail(mail)

    if not(result[0]):
        mail.sendmail(sender,result[1])
    else:
        pass #somedb work

    print('All done')

if __name__ == '__main__':
    run_project(sys.argv)