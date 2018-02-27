def test_post_push(client, sample_payload_push, minion_mock, client_caller):
    result = client.simulate_post('/bitbucket/events', json=sample_payload_push)
    assert minion_mock.called
    assert result.status_code == 200

def test_post_push_invalid_payload(client, minion_mock, client_caller):
    result = client.simulate_post('/bitbucket/events', json={})
    assert result.status_code == 400
    assert result.json == {'description': 'key "eventKey" is not provided', 'title': 'Invalid payload'}