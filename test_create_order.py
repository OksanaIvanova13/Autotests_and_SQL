import sender_stand_request
import data


def test_create_order():
    create_response = sender_stand_request.post_new_order(data.order_body)

    track = create_response.json()["track"]

    get_response = sender_stand_request.get_order(track)

    assert get_response.status_code == 200