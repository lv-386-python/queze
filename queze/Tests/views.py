import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from Tests.models import Test, Question, Answer, Results, UserAnswer


@require_http_methods(["POST"])
def create_test(request):
    data = json.loads(request.body)
    user = request.user
    test = Test.create(data['test_name'], data['test_description'], user)
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
    test.update_test(test, data['test_name'], data['test_description'], request.user)
    if test:
        return HttpResponse("Successfully updated", status=204)
    return HttpResponse(status=400)


@require_http_methods(["DELETE"])
def delete_test(request, test_id):
    is_deleted = Test.delete_test(test_id)
    if is_deleted:
        return HttpResponse('Deleted.', status=204)
    return HttpResponse(status=404)


@require_http_methods(["POST"])
def create_question(request):
    data = json.loads(request.body)
    user = request.user
    test = request.test
    question = Question.create_quest(data['question_text'], user, test)
    if question:
        return HttpResponse(status=201)
    return HttpResponse(status=400)


@require_http_methods(["GET"])
def get_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Exception:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(question))


@require_http_methods(["PUT"])
def update_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Exception:
        return HttpResponse(status=404)
    data = json.loads(request.body)
    question.question_text = data['question_text']
    try:
        question.save()
        return JsonResponse({'message': 'Question was successfully updated.'}, status=204)
    except Exception:
        HttpResponse(status=400)


@require_http_methods(["DELETE"])
def delete_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Exception:
        return HttpResponse(status=404)
    question.delete()
    return JsonResponse({'message': 'Question was successfully deleted.'}, status=204)


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
    try:
        answer = Answer.objects.get(pk=answer_id)
    except Exception:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(answer))


@require_http_methods(["PUT"])
def update_answer(request, answer_id):
    try:
        answer = Answer.objects.get(pk=answer_id)
    except Exception:
        return HttpResponse(status=404)
    data = json.loads(request.body)
    answer.answer_text = data['answer_text']
    try:
        answer.save()
        return JsonResponse({'message': 'Answer was successfully updated.'}, status=204)
    except Exception:
        return HttpResponse(status=400)


@require_http_methods(["DELETE"])
def delete_answer(request, answer_id):
    try:
        answer = Answer.objects.get(pk=answer_id)
    except Exception:
        return HttpResponse(status=404)
    answer.delete()
    return JsonResponse({'message': 'Answer was successfully deleted.'}, status=204)


@require_http_methods(["GET"])
def get_results(request, test_id):
    try:
        result = Results.objects.format(result_test=test_id)
    except Exception:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(result))

@require_http_methods(["POST"])
def create_user_answer(request):
    data = json.loads(request.body)
    user = request.user
    test = request.test
    user_answer = UserAnswer.create_quest(data["question"], user, test)
    if user_answer:
        return HttpResponse(status=201)
    return  HttpResponse(status=404)

@require_http_methods(["GET"])
def get_user_answer(request, user_answer_id):
    try:
        user_answer = UserAnswer.object.get(user_answer_id)
    except Exception:
        return HttpResponse(status=404)
    return JsonResponse(model_to_dict(user_answer))

@require_http_methods(["PUT"])
def update_user_answer(request, user_answer_id):
    try:
        user_answer = UserAnswer.object.get(id=user_answer_id)
    except Exception:
        return HttpResponse(status=404)
    data = json.loads(request.body)
    user_answer.question = data["question"]
    try:
        user_answer.save()
        return JsonResponse({'message': 'Answer was successfully updated.'}, status=204)
    except Exception:
        return HttpResponse(status=404)