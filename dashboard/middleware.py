from django.shortcuts import reverse, HttpResponseRedirect

class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
        
    def process_request(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('home') # or http response
        return None