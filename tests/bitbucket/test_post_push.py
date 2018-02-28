def test_post_modified(client, sample_payload_push, minion_mock, salt_event_send):
    result = client.simulate_post('/bitbucket/events', json=sample_payload_push)
    minion_mock.assert_called_once()
    salt_event_send.assert_called_once_with('/bitbucket/event/push', sample_payload_push)
    assert result.status_code == 200


def test_post_push_invalid_payload(client, minion_mock, salt_event_send):
    result = client.simulate_post('/bitbucket/events', json={})
    assert minion_mock.called == False
    assert salt_event_send.called == False
    assert result.status_code == 400
    assert result.json == {'description': 'key "eventKey" is not provided', 'title': 'Invalid payload'}
