from rest_framework.throttling import SimpleRateThrottle

class CustomThrottle(SimpleRateThrottle):
    scope = 'user_requests'

    def get_cache_key(self, request, view):
        return self.get_ident(request)

    def allow_request(self, request, view):
  
        if not hasattr(self, 'history'):
            self.history = []

        return super().allow_request(request, view)
