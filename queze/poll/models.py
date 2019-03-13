from django.db import IntegrityError
from django.db import models

from authentification.models import CustomUser


class Test(models.Model):
    ''' Model for Test.
        id field is generated automatically by Django
    '''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    @staticmethod
    def create(name, description, user):
        test = Test()
        test.name = name
        test.description = description
        test.author = user
        try:
            test.save()
            return test
        except (ValueError, IntegrityError):
            pass

    @staticmethod
    def update_test(test_instance, name, description, user):
        test = test_instance
        test.name = name
        test.description = description
        test.author = user
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
