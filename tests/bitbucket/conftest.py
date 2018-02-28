import pytest


@pytest.fixture(scope='function')
def sample_payload_push():
    payload = {
        'eventKey': 'repo:refs_changed',
        'date': '2017-09-19T09:45:32+1000',
        'actor': {
            'name': 'admin',
            'emailAddress': 'admin@example.com',
            'id': 1,
            'displayName': 'Administrator',
            'active': True,
            'slug': 'admin',
            'type': 'NORMAL'
        },
        'repository': {
            'slug': 'repository',
            'id': 84,
            'name': 'repository',
            'scmId': 'git',
            'state': 'AVAILABLE',
            'statusMessage': 'Available',
            'forkable': True,
            'project': {
                'key': 'PROJ',
                'id': 84,
                'name': 'project',
                'public': False,
                'type': 'NORMAL'
            },
            'public': False
        },
        'changes': [
            {
                'ref': {
                    'id': 'refs/heads/master',
                    'displayId': 'master',
                    'type': 'BRANCH'
                },
                'refId': 'refs/heads/master',
                'fromHash': 'ecddabb624f6f5ba43816f5926e580a5f680a932',
                'toHash': '178864a7d521b6f5e720b386b2c2b0ef8563e0dc',
                'type': 'UPDATE'
            }
        ]
    }
    return payload


@pytest.fixture(scope='function')
def sample_payload_modified():
    payload = {
        'eventKey': 'repo:modified',
        'date': '2017-09-19T09:51:20+1000',
        'actor': {
            'name': 'admin',
            'emailAddress': 'admin@example.com',
            'id': 1,
            'displayName': 'Administrator',
            'active': True,
            'slug': 'admin',
            'type': 'NORMAL'
        },
        'old': {
            'slug': 'repository',
            'id': 84,
            'name': 'repository',
            'scmId': 'git',
            'state': 'AVAILABLE',
            'statusMessage': 'Available',
            'forkable': True,
            'project': {
                'key': 'PROJ',
                'id': 84,
                'name': 'project',
                'public': False,
                'type': 'NORMAL'
            },
            'public': False
        },
        'new': {
            'slug': 'repository2',
            'id': 84,
            'name': 'repository2',
            'scmId': 'git',
            'state': 'AVAILABLE',
            'statusMessage': 'Available',
            'forkable': True,
            'project': {
                'key': 'PROJ',
                'id': 84,
                'name': 'project',
                'public': False,
                'type': 'NORMAL'
            },
            'public': False
        }
    }
    return payload


@pytest.fixture(scope='function')
def salt_event_send(mocker):
    event_send = mocker.patch('salt.modules.event.send', autospec=True)
    return event_send


@pytest.fixture(scope='function')
def minion_mock(mocker, salt_event_send):
    minion = mocker.patch('salt.minion.SMinion', autospec=True)
    minion.return_value.functions = {'event.send': salt_event_send}
    return minion


@pytest.fixture(scope='function')
def send_event_call_push(mocker):
    expected_calls = [mocker.call({'tag': '/bitbucket/event/push'})]
    return expected_calls
