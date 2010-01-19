from Worker import Worker
import e3

class Session(e3.Session):
    '''a specialization of e3.Session'''
    NAME = 'Gtalk session'
    DESCRIPTION = 'Session to connect to the Jabber network (Gtalk servers)'
    AUTHOR = 'Mariano Guerra'
    WEBSITE = 'www.emesene.org'

    def __init__(self, id_=None, account=None):
        '''constructor'''
        e3.Session.__init__(self, id_, account)

    def login(self, account, password, status, proxy, use_http=False):
        '''start the login process'''
        self.account = e3.Account(account, password, status)
        worker = Worker('emesene2', self, proxy, use_http)
        worker.start()

        self.actions.login(account, password, status)

    def send_message(self, cid, text, style=None):
        '''send a common message'''
        account = self.account.account
        message = e3.Message(e3.Message.TYPE_MESSAGE, text, account,
            style)
        self.actions.send_message(cid, message)

    def request_attention(self, cid):
        '''request the attention of the contact'''
        account = self.account.account
        message = e3.Message(e3.Message.TYPE_MESSAGE,
            '%s requests your attention' % (account, ), account)
        self.actions.send_message(cid, message)
