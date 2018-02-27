import salt.client

class BitbucketEvent(object):
    def __init__(self, data):
        self.tag = '/bitbucket/event'
        self.data = data
        self.caller = salt.client.Caller()

    def send(self):
        self.caller.cmd('event.send', self.tag, self.data)


class PushEvent(BitbucketEvent):
    def __init__(self, data):
        BitbucketEvent.__init__(self, data)
        self.tag = '/bitbucket/event/push'

class ModifiedEvent(BitbucketEvent):
    def __init__(self, data):
        BitbucketEvent.__init__(self, data)
        self.tag = '/bitbucket/event/modified'


class PullrequestEvent(BitbucketEvent):
    def __init__(self, data):
        BitbucketEvent.__init__(self, data)
        self.tag = '/bitbucket/event/pullrequest'
