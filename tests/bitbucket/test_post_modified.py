def test_post_modified(client, sample_payload_modified, minion_mock, client_caller):
    result = client.simulate_post('/bitbucket/events', json=sample_payload_modified)
    assert minion_mock.called
    assert result.status_code == 200

