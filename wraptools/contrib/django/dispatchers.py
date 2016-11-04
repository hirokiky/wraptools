def is_authenticated(request, *args, **kwargs):
    """ Dispatcher for django views functions to dispatch to authentication views
    """
    return request.user.is_authenticated
