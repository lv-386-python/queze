from django.db import IntegrityError
from django.db import models

from authentification.models import CustomUser
from poll.models import Test


class Results(models.Model):
    'Class with score of the test'
    score = models.IntegerField(default=1)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="results")
    passer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="results")
    completion_date = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def calculate_result(user, test):
        pass

    @staticmethod
    def create(test_id, question_id, user_id):
        results = Results()
        results.score = 1
        results.test = test_id
        results.passer = user_id
        try:
            results.save()
            return results
        except (ValueError, IntegrityError):
            pass

    @staticmethod
    def delete(result_id):
        result = Results.get(result_id)
        if result:
            result.delete()
            return True
        return False

    @staticmethod
    def get_score(test_id):
        try:
            test = Results.objects.get(test=test_id)
        except Results.DoesNotExist:
            print('Result does not exist')
            return False
        return test
