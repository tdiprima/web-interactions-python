# This function attempts to retrieve a JWT access token from a specified host and handles potential exceptions.
# https://gist.githubusercontent.com/jhsu98
import requests


def get_access_token(self):
    # the function that is
    # used to request the JWT
    try:
        # TODO: build the JWT and store
        # in the variable `token_body`
        token_body = {}

        # request an access token
        request = requests.post(self.host, data=token_body)

        # optional: raise exception for status code
        request.raise_for_status()
    except Exception as e:
        print(e)
        return None
    else:
        # assuming the response's structure is
        # {"token": ""}
        return request.json()['token']
