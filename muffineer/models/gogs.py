import salt.client

class GogsEvent(object):
    def __init__(self, data):
        self.tag = '/gogs/event'
        self.data = data
        self.caller = salt.client.Caller()

    def send(self):
        self.caller.cmd('event.send', self.tag, self.data)


class PushEvent(GogsEvent):
    def __init__(self, data):
        GogsEvent.__init__(self, data)
        self.tag = '/gogs/event/push'
