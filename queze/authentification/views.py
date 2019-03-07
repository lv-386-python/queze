import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from authentification.models import CustomUser

@require_http_methods(["POST"])
def registration(request):

    data = json.loads(request.body)
    print(data)
    user = CustomUser.create(data['email'], data['password'])
    if user:
        return HttpResponse(status=201)
    return HttpResponse(status=400)

@require_http_methods(["POST"])
def log_in(request):
    data = json.loads(request.body)
    print(data)
    user = authenticate(email=data['email'], password=data['password'])
    print(user)
    if not user:
        return HttpResponse(status=400)
    login(request, user=user)
    return HttpResponse(status=200)


@require_http_methods(["POST"])
def log_out(request):
    print(request.user)
    logout(request)
    return HttpResponse(status=200)

