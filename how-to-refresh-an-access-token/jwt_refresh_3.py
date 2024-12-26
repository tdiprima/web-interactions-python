# Initializes an instance of a class with host, key, and secret attributes, requests an access token and sets its
# expiration time 3500 seconds from the current time. An exception is raised if the access token is not obtained.
# https://gist.githubusercontent.com/jhsu98
import time


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
