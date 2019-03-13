import json
from django.db import IntegrityError
from django.db import models
from django.forms import model_to_dict
from django.http import JsonResponse
from django.http import HttpResponse

from authentification.models import CustomUser
from question.models import Question
from answer.models import Answer
from results.models import Results


class UserAnswer(models.Model):
    'Class with answer for user'
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    result = models.ForeignKey(Results, on_delete=models.CASCADE, related_name='user_answers')

    @staticmethod
    def create_user_answer(text, user, answer):
        'Create answer for user'
        user_answer = UserAnswer()
        user_answer.question = text
        user_answer.user = user
        user_answer.answer = answer

        try:
            user_answer.save()
            return user_answer
        except (ValueError, IntegrityError):
            pass

    @staticmethod
    def get_user_answer(request, user_answer_id):
        'Get answer for user'
        try:
            user_answer = UserAnswer.object.get(user_answer_id)
        except Exception:
            return HttpResponse(status=404)
        return JsonResponse(model_to_dict(user_answer))

    @staticmethod
    def update_user_answer(request, user_answer_id):
        'Update answer for user'
        try:
            user_answer = UserAnswer.object.get(id=user_answer_id)
        except Exception:
            return HttpResponse(status=404)
        data = json.loads(request.body)
        user_answer.question = data["question"]
        try:
            user_answer.save()
            return JsonResponse({'message': 'User answer was successfully updated.'}, status=204)
        except Exception:
            return HttpResponse(status=404)
