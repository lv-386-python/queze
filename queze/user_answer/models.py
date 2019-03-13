from django.db import IntegrityError
from django.db import models

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
        user_answer = UserAnswer()
        user_answer.question = text
        user_answer.user = user
        user_answer.answer = answer

        try:
            user_answer.save()
            return user_answer
        except (ValueError, IntegrityError):
            pass
