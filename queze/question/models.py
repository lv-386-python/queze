from django.db import IntegrityError
from django.db import models

from poll.models import Test
from authentification.models import CustomUser


class Question(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="questions")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")

    @staticmethod
    def create(text, user, key):
        question = Question()
        question.text = text
        question.author = user
        question.test = key
        try:
            question.save()
            return question
        except (ValueError, IntegrityError):
            pass
