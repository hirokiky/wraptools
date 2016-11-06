def is_authenticated(request, *args, **kwargs):
    """ Dispatcher for django views functions to dispatch to authentication views
    """
    return request.user.is_authenticated


def method(method_name):
    """ Dispatcher to route when request.method is same with :param method_name:
    """
    def dispatcher(request, *args, **kwargs):
        return request.method == method_name
    return dispatcher


method_get = method("GET")
method_post = method("POST")
method_put = method("PUT")
method_delete = method("DELETE")
