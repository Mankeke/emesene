import e3
from Worker import Worker
from MsnMessage import Message
import extension

class Session(e3.Session):
    '''a specialization of e3.Session'''
    NAME = 'MSN session'
    DESCRIPTION = 'Session to connect to the MSN network'
    AUTHOR = 'Mariano Guerra'
    WEBSITE = 'www.emesene.org'

    def __init__(self, id_=None, account=None):
        '''constructor'''
        e3.Session.__init__(self, id_, account)

    def login(self, account, password, status, proxy, use_http=False):
        '''start the login process'''
        worker = Worker('emesene2', self, proxy, use_http)
        worker.start()

        self.account = e3.Account(account, password, status)

        self.actions.login(account, password, status)

    def send_message(self, cid, text, style=None):
        '''send a common message'''
        account = self.account.account
        message = Message(Message.TYPE_MESSAGE, text, account, style)
        self.actions.send_message(cid, message)

    def request_attention(self, cid):
        '''send a nudge message'''
        account = self.account.account
        message = e3.Message(Message.TYPE_NUDGE, None, account)
        self.actions.send_message(cid, message)

extension.implements(Session, 'session')
