from functools import wraps


def dispatch(dispatchers, default=None):
    """ Dispatch
    """
    def dec(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            for dispatcher in dispatchers:
                if dispatcher(*args, **kwargs):
                    return func(*args, **kwargs)
            if default:
                return default(*args, **kwargs)
        return wrapped
    return dec
