from django.db import models
from ..authentification.models import CustomUser


# Create your models here.
class Test(models.Model):
    'Model for Test'
    # id field is generated authomatically by Django
    test_name = models.CharField(max_length=35)
    test_description = models.CharField(max_length=140)
    test_author = artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE)