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
