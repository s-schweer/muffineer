def test_post_modified(client, sample_payload_push, minion_mock, salt_event_send):
    headers = {'X-Gogs-Signature': 'wtfalter'}
    result = client.simulate_post('/gogs/events', json=sample_payload_push, headers=headers)
    minion_mock.assert_called_once()
    salt_event_send.assert_called_once_with('/gogs/event/push', sample_payload_push)
    assert result.status_code == 200


def test_post_push_no_signature(client, minion_mock, salt_event_send):
    result = client.simulate_post('/gogs/events', json={})
    assert minion_mock.called == False
    assert salt_event_send.called == False
    assert result.status_code == 400
    assert result.json == {'description': 'The X-Gogs-Signature header is required.',
                           'title': 'Missing header value'}
