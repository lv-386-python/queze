from django.db import IntegrityError
from django.db import models

from authentification.models import CustomUser


# Create your models here.
class Test(models.Model):
    'Model for Test'
    # id field is generated authomatically by Django
    test_name = models.CharField(max_length=35)
    test_description = models.CharField(max_length=140)
    test_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    @staticmethod
    def create(name, description, user):
        test = Test()
        test.test_name = name
        test.test_description = description
        test.test_author = user
        try:
            test.save()
            return test
        except (ValueError, IntegrityError):
            pass


class Answer(models.Model):
    'Asnwers for Questions'
    answer_text = models.ForeignKey(Question, on delete=models.CASCADE)
    answer_auther = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    is_correct = models.BooleanField(default=False)
    
    @staticmethod
    def create_answer(text, user, correctly):
        answer = Answer()
        answer.answer_text = text
        answer.answer_auther = user
        answer.is_correct = correctly
        try:
            answer.save()
            return answer
        except (ValueError, IntegerityError):
            pass


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    question_test = models.ForeignKey(Test, on_delete=models.CASCADE, default=1)

    @staticmethod
    def create_quest(text, user, key):
        question = Question()
        question.question_text = text
        question.question_author = user
        question.question_test = key
        try:
            question.save()
            return question
        except (ValueError, IntegrityError):
            pass


class Results(models.Model):
    pass


class UserAnswer(models.Model):
    user = models.ForeignKey(CustomUser)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)

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
