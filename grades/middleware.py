from django.middleware.security import SecurityMiddleware


class CustomSecurityMiddleware(SecurityMiddleware):
    def process_request(self, request):
        # Implementasi tambahan keamanan
        pass
