from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
# prevent page cache-ing
# import this in setting middleware

class NoCacheMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    

# expiring session when restaring server
class SessionExpiryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        server_session_key = settings.SESSION_EXPIRY_KEY
        session_server_key = request.session.get('server_session_key', None)

        if session_server_key != server_session_key:
            request.session.flush()  # Log out the user
            request.session['server_session_key'] = server_session_key