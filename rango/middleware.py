from rango import current_db


class MultiHostDBRouterMiddleware(object):
    """
    The Host DB router middelware.

    The middleware process_view (or process_request) function sets some context
    from the URL into thread local storage, and process_response deletes it. In
    between, any database operation will call the router, which checks for this
    context and returns an appropriate database alias.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_db.db = self._find_request_host(request)

        response = self.get_response(request)

        return response

    @staticmethod
    def _find_request_host(request):
        return request.META.get('HTTP_HOST')
