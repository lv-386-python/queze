import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from user_answer.models import UserAnswer

@require_http_methods(["POST"])
def create_user_answer(request):
    'Create answer for user'
    data = json.loads(request.body)
    user = request.user
    test = request.test
    user_answer = UserAnswer.create_user_answer(data["question"], user, test)
    if user_answer:
        return HttpResponse(status=201)
    return  HttpResponse(status=404)

@require_http_methods(["GET"])
def get_user_answer(request, user_answer_id):
    'Get answer for user'
    user_answer = UserAnswer.object.get(user_answer_id)
    if user_answer:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(user_answer))

@require_http_methods(["PUT"])
def update_user_answer(request, user_answer_id):
    'Update answer for user'
    user_answer = UserAnswer.object.get(id=user_answer_id)
    if not user_answer:
        return HttpResponse(status=404)
    data = json.loads(request.body)
    user_answer.update_user_answer = data["question"]
    if user_answer:
        return JsonResponse({'message': 'User answer was successfully updated.'}, status=204)
    return HttpResponse(status=404)
