import pytest

def test_get_health(client):

    result = client.simulate_get('/health')
    assert result.status_code == 200

