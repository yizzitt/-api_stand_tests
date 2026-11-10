import requests
import configuration


def post_new_user(user_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=user_body
    )