import json

import pytest
from falcon import testing

from muffineer import api


@pytest.fixture(scope='module')
def client():
    # Assume the hypothetical `myapp` package has a
    # function called `create()` to initialize and
    # return a `falcon.API` instance.
    config = dict()
    return testing.TestClient(api.create(config=config))


def test_get_config(client):

    result = client.simulate_get('/health')
    assert result.json == doc
