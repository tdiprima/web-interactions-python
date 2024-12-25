# https://gist.githubusercontent.com/jhsu98
import time


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
