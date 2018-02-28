def test_post_modified(client, sample_payload_modified, minion_mock, salt_event_send):
    result = client.simulate_post('/bitbucket/events', json=sample_payload_modified)
    minion_mock.assert_called_once()
    salt_event_send.assert_called_once_with('/bitbucket/event/modified', sample_payload_modified)
    assert result.status_code == 200
