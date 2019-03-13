from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from results.models import Results


@require_http_methods(["GET"])
def get_result(request, test_id):
    try:
        result = Results.get_score(test_id=test_id)
    except Exception:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(result))
