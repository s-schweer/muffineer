import json

import pytest
from falcon import testing

from gazetteer import api


@pytest.fixture(scope='module')
def client():
    # Assume the hypothetical `myapp` package has a
    # function called `create()` to initialize and
    # return a `falcon.API` instance.
    config = dict(foo='bar',
                  dns_server='172.17.0.2',
                  domains=['example.net'])
    return testing.TestClient(api.create(config=config))


def test_get_config(client):
    doc = dict(foo='bar',
               dns_server='172.17.0.2',
               domains=['example.net'])

    result = client.simulate_get('/config')
    assert result.json == doc


def test_get_domains(client):
    result = client.simulate_get('/zones')
    domains = ['example.net']
    assert result.json == domains


def test_head_domain_exists(client):
    result = client.simulate_head('/zones/example.net')
    assert result.status == '200 OK'


def test_head_domain_not_exists(client):
    result = client.simulate_head('/zones/example.com')
    assert result.status == '404 Not Found'


def test_get_domain(client):
    doc = {"ftp": "ftp 86400 IN CNAME www", "www": "www 86400 IN A 192.168.0.2",
           "@": "@ 86400 IN SOA ns1 hostmaster 2002022401 10800 15 604800 10800; @ 86400 IN NS ns1; @ 86400 IN MX 10 mail.another.com.",
           "ns1": "ns1 86400 IN A 192.168.0.1", "bill": "bill 86400 IN A 192.168.0.3",
           "fred": "fred 86400 IN A 192.168.0.4"}

    result = client.simulate_get('/zones/example.net')
    assert result.json == doc


def test_get_records(client):
    doc = {"a_records": [{"name": "bill", "ttl": "86400", "address": "192.168.0.3"},
                         {"name": "fred", "ttl": "86400", "address": "192.168.0.4"},
                         {"name": "ns1", "ttl": "86400", "address": "192.168.0.1"},
                         {"name": "www", "ttl": "86400", "address": "192.168.0.2"}],
           "cname_records": [{"name": "ftp", "ttl": "86400", "address": "www"}]}
    result = client.simulate_get('/zones/example.net/records')
    assert result.json == doc


def test_head_existing_a_record(client):
    result = client.simulate_head('/zones/example.net/records/bill')
    assert result.status == '200 OK'


def test_head_non_existing_a_record(client):
    result = client.simulate_head('/zones/example.net/records/alter')
    assert result.status == '404 Not Found'


def test_get_existing_a_record(client):
    doc = {'name': 'bill', 'address': '192.168.0.3', 'ttl': '86400', 'record_type': 'A'}
    result = client.simulate_get('/zones/example.net/records/bill')
    assert result.json == doc


def test_post_a_record(client):
    a_record = json.dumps({'name': 'horst', 'address': '192.168.0.15', 'ttl': 86400, 'record_type': 'A'})
    headers = {'Content-Type': 'application/json'}
    result = client.simulate_post('/zones/example.net/records', body=a_record, headers=headers)
    assert result.headers.get('location') == '/zones/example.net/records/horst'


def test_put_for_existing_a_record(client):
    a_record = json.dumps({'name': 'horst', 'address': '192.168.0.16', 'ttl': 86400, 'record_type': 'A'})
    headers = {'Content-Type': 'application/json'}
    result = client.simulate_put('/zones/example.net/records/horst', body=a_record, headers=headers)
    assert result.status == '204 No Content'


def test_put_for_non_existing_a_record(client):
    a_record = json.dumps({'name': 'hugo', 'address': '192.168.0.17', 'ttl': 86400, 'record_type': 'A'})
    headers = {'Content-Type': 'application/json'}
    result = client.simulate_put('/zones/example.net/records/hugo', body=a_record, headers=headers)
    assert result.status == '201 Created'


def test_delete_existing_a_record(client):
    result = client.simulate_delete('/zones/example.net/records/hugo')
    assert result.status == '200 OK'


def test_delete_non_existing_a_record(client):
    result = client.simulate_delete('/zones/example.net/records/schwede')
    assert result.status == '404 Not Found'


def test_get_a_records_after_manipulation(client):
    doc = {"a_records": [{"name": "horst", "address": "192.168.0.16", "ttl": "86400"},
                         {"name": "bill", "address": "192.168.0.3", "ttl": "86400"},
                         {"name": "fred", "address": "192.168.0.4", "ttl": "86400"},
                         {"name": "ns1", "address": "192.168.0.1", "ttl": "86400"},
                         {"name": "www", "address": "192.168.0.2", "ttl": "86400"}],
           "cname_records": [{"name": "ftp", "address": "www", "ttl": "86400"}]}
    result = client.simulate_get('/zones/example.net/records')
    assert result.json == doc


def test_change_existing_a_record_to_cname(client):
    record = json.dumps({'name': 'horst', 'address': 'bill', 'ttl': 86400, 'record_type': 'CNAME'})
    headers = {'Content-Type': 'application/json'}
    result = client.simulate_put('/zones/example.net/records/horst', body=record, headers=headers)
    assert result.status == '204 No Content'
