def dispatch(*dispatchers, default=None):
    """ Dispatch

    :arg dispatchers: will be a iterable of pair tuple
    which has dispatcher function as first element
    and target function as second element.

    The dispatcher function will take same arguments with target functions
    and will return True or False.
    When it is a True, corresponding target function will be called.

    >>> f = dispatch(
    ...     (lambda x: x % 2, lambda x: str(x) + "is odd"),
    ...     default=lambda x: str(x) + "is even",
    ... )
    ...
    >>> print(f(3))  # say 3 is odd

    :arg default: function will be called if all of dispatchers will return False.
    default function is optional so when default is not specified, it will return None.
    """
    def wrapped(*args, **kwargs):
        for dispatcher, func in dispatchers:
            if dispatcher(*args, **kwargs):
                return func(*args, **kwargs)

        if default:
            return default(*args, **kwargs)

    return wrapped
