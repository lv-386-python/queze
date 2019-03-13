from django.db import IntegrityError
from django.db import models
from django.utils import timezone

from authentification.models import CustomUser


# Create your models here.
class Test(models.Model):
    'Model for Test'
    # id field is generated authomatically by Django
    test_name = models.CharField(max_length=50)
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

    @staticmethod
    def update_test(test_instance, name, description, user):
        test = test_instance
        test.test_name = name
        test.test_description = description
        test.test_author = user
        try:
            test.save()
            return test
        except (ValueError, IntegrityError):
            pass


    @staticmethod
    def delete_test(test_id):
        test = Test.get_by_id(test_id)
        if test:
            test.delete()
            return True
        return False


    @staticmethod
    def get_by_id(test_id):
        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            print('Not found')
            return False
        return test


