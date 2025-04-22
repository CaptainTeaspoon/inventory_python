from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import get_user

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = reverse('login')
        self.exempt_urls = [reverse('login'), reverse('register')]  # URLs, die keine Anmeldung erfordern

    def __call__(self, request):
        user = get_user(request)
        if not user.is_authenticated and request.path_info not in self.exempt_urls:
            return redirect(self.login_url)
        response = self.get_response(request)
        return response