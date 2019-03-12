import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from authentification.models import CustomUser


@require_http_methods(["POST"])
def registration(request):
    data = json.loads(request.body)
    user = CustomUser.create(data['email'], data['password'])
    if user:
        return HttpResponse(status=201)
    return HttpResponse(status=400)


@require_http_methods(["POST"])
def log_in(request):
    data = json.loads(request.body)
    user = authenticate(email=data['email'], password=data['password'])
    if not user:
        return HttpResponse(status=400)
    login(request, user=user)
    return HttpResponse(status=200)


@require_http_methods(["POST"])
def log_out(request):
    logout(request)
    return HttpResponse(status=200)


@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    is_deleted = CustomUser.delete_by_id(user_id)
    if is_deleted:
        return HttpResponse('deleted', status=204)
    return HttpResponse(status=404)


@require_http_methods(["GET"])
def get_user(request, user_id):
    is_get = CustomUser.get(user_id)
    if is_get:
        return JsonResponse(is_get, status=201)
    return HttpResponse(status=404)

@require_http_methods(["PUT"])
def update_user(request, user_id):
    data = json.loads(request.body)
    updated_user = CustomUser.update(user_id, data)
    if updated_user:
        return HttpResponse(status=204)
    HttpResponse(status=400)
