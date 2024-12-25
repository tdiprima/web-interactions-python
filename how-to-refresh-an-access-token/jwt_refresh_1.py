# Establishes a class called MyApi that includes attributes for host, key, secret, access token, and access token expiration, with methods for initializing a new instance of the class and getting an access token, alongside a dedicated decorators class for refreshing tokens when necessary.
# https://gist.githubusercontent.com/jhsu98
class MyApi:
    host = None
    key = None
    secret = None
    access_token = None
    access_token_expiration = None

    def __init__(self, host, key, secret):
        # the function that is executed when
        # an instance of the class is created
        pass

    def get_access_token(self):
        # the function that is
        # used to request the JWT
        pass

    class Decorators:
        @staticmethod
        def refresh_token(decorated):
            # the function that is used to check
            # the JWT and refresh if necessary
            pass
