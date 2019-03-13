import json
from django.db import IntegrityError
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.utils import timezone

from authentification/models.py import CustomUser



class Answer(models.Model):
    'Asnwers for Questions'

    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    answer_text = models.TextField(default=1)
    answer_auther = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


    @staticmethod
    def create_answer(question, text, user, correctly):
        answer = Answer()

        answer.question_id = question
        answer.answer_text = text
        answer.answer_auther = user
        answer.is_correct = correctly
        try:
            answer.save()
            return answer
        except (ValueError, IntegrityError):
            pass


    @staticmethod
    def get_answer(request, answer_id):
        try:
            answer = Answer.objects.get(pk=answer_id)
        except Exception:
            return HttpResponse(status=404)
        return JsonResponse(model_to_dict(answer))


    @@staticmethod
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


    @staticmethod
    def delete_answer(answer_id):
        answer = Answer.get_by_id(answer_id)
        if answer:
            answer.delete()
            return True
        return False


    @staticmethod
    def get_by_id(answer_id):
        try:
            answer = Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            print('Not found')
            return False
        return answer


