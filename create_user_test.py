import data
import sender_stand_request


def positive_assert(first_name):
    user_body = data.user_body.copy()
    user_body["firstName"] = first_name

    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 201


def negative_assert_symbol(first_name):
    user_body = data.user_body.copy()
    user_body["firstName"] = first_name

    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400


def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaa")


def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")