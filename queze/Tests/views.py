import json

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from Tests.models import Test


@require_http_methods(["POST"])
def create_test(request):
    data = json.loads(request.body)
    user = request.user
    test = Test.create(data['test_name'], data['test_description'], user)
    if test:
        return HttpResponse(status=201)

    return HttpResponse(status=400)
