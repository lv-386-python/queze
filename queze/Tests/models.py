from django.db import IntegrityError
from django.db import models
from django.utils import timezone

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


class Question(models.Model):
    question_text = models.CharField(max_length=200, default=1)
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


class Answer(models.Model):
    'Asnwers for Questions'
    answer_text = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
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
        except (ValueError, IntegrityError):
            pass


class Results(models.Model):
    'Class with results of the test'
    score = models.IntegerField(default=0)
    result_test = models.ForeignKey(Test, on_delete=models.CASCADE, default=1)
    result_passer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    completion_date = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_result(test_id, question_id, user_id):
        results = Results()
        results.score = 0
        results.result_test = test_id
        results.result_passer = user_id
        # getting all questions from required test
        questions = Question().objects.filter(pk=test_id)
        # getting all correct answers
        for q in questions:
            if Answer().objects.filter(pk=q.question_id).filter(is_correct=True):
                results.score += 1
        try:
            results.save()
            return results
        except (ValueError, IntegrityError):
            pass


class UserAnswer(models.Model):
    pass
