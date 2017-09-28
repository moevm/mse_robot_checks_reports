"""verify mails"""
class Verifier:
    """verify mails"""    
    def __init__(self):
        pass

    def verifymail(self, mail):
        if self.verifyname(mail['mailname']):
            return (True,'')
        else:
            return (False,'invalid name')

        if self.verifydata(mail['data']):
            return (True,'')
        else:
            return (False,'invalid data')


    def verifyname(self, mailname):
        if mailname == 'name':
            return True
        else:
            return False

    def verifydata(self, data):
        if data == 'data':
            return True
        else:
            return False