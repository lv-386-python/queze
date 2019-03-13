import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from poll.models import Test


@require_http_methods(["POST"])
def create_test(request):
    data = json.loads(request.body)
    user = request.user
    test = Test.create(data['name'], data['description'], user)
    if test:
        return HttpResponse(status=201)
    return HttpResponse(status=400)


@require_http_methods(["GET"])
def get_test(request, test_id):
    test = Test.get_by_id(test_id)
    if not test:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(test))


@require_http_methods(["PUT"])
def update_test(request, test_id):
    test = Test.get_by_id(test_id)
    if not test:
        return HttpResponse(status=404)
    data = json.loads(request.body)
    test.update_test(test, data['name'], data['description'], request.user)
    if test:
        return HttpResponse("Successfully updated", status=204)
    return HttpResponse(status=400)


@require_http_methods(["DELETE"])
def delete_test(request, test_id):
    is_deleted = Test.delete_test(test_id)
    if is_deleted:
        return HttpResponse('Deleted.', status=204)
    return HttpResponse(status=404)
