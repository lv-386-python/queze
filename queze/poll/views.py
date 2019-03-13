import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from poll.models import Answer




@require_http_methods(["POST"])
def create_answer(request):
    data = json.loads(request.body)
    user = request.user
    test = request.test
    answer = Answer.create_quest(data['answer_text'], user, test)
    if answer:
        return HttpResponse(status=201)
    return HttpResponse(status=400)


@require_http_methods(["GET"])
def get_answer(request, answer_id):
    answer = Answer.get_by_id(answer_id)
    if not answer:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(answer))


@require_http_methods(["PUT"])
def update_answer(request, answer_id):
    answer = Answer.get_by_id(answer_id)
    if not answer:
        return HttpResponse(status=404)
    data = json.loads(request.body)
    answer.update_answer = data['answer_text']
    if answer:
        return HttpResponse('Answer was successfully updated', status=204)
    return HttpResponse(status=400)


@require_http_methods(["DELETE"])
def delete_answer(request, answer_id):
    is_deleted = Answer.delete_answer(answer_id)
    if is_deleted:
        return HttpResponse('Deleted', status=204)
    return HttpResponse(status=404)




