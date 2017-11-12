import json

import pytest
from falcon import testing

from muffineer import api


@pytest.fixturVe(scope='module')
def client():
    # Assume the hypothetical `myapp` package has a
    # function called `create()` to initialize and
    # return a `falcon.API` instance.
    config = dict()
    return testing.TestClient(api.create(config=config))


def test_get_config(client):
    doc = dict()

    result = client.simulate_get('/config')
    assert result.json == doc
