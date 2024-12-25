# https://gist.githubusercontent.com/jhsu98
import time
import requests


class MyApi:
    host = None
    key = None
    secret = None
    access_token = None
    access_token_expiration = None

    def __init__(self, host, key, secret):
        # the function that is executed when
        # an instance of the class is created
        self.host = host
        self.key = key
        self.secret = secret

        try:
            self.access_token = self.get_access_token()
            if self.access_token is None:
                raise Exception("Request for access token failed.")
        except Exception as e:
            print(e)
        else:
            self.access_token_expiration = time.time() + 3500

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

    class Decorators:
        @staticmethod
        def refresh_token(decorated):
            # the function that is used to check
            # the JWT and refresh if necessary
            def wrapper(api, *args, **kwargs):
                if time.time() > api.access_token_expiration:
                    api.get_access_token()
                return decorated(api, *args, **kwargs)

            return wrapper

    @Decorators.refresh_token
    def some_request(self):
        # make our API request
        pass
