import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

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


@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    try:
        user = CustomUser.object.get(pk=user_id)
    except Exception:
        return HttpResponse(status=404)
    user.delete()
    return HttpResponse(status=204)


@require_http_methods(["GET"])
def get_user(request, user_id):
    try:
        user = CustomUser.object.get(pk=user_id)
    except Exception:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(user), status=201)


@require_http_methods(["PUT"])
def update_user(request, user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
    except:
        print('not found')
        return HttpResponse(status=404)
    data = json.loads(request.body)
    user.email = data['new_email']
    user.password = data['new_password']
    try:
        user.save()
        return HttpResponse(status=204)
    except:
        HttpResponse(status=400)
