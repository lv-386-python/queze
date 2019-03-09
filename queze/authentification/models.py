from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import IntegrityError


# Create your models here.


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    object = BaseUserManager()

    @staticmethod
    def create(email, password):
        user = CustomUser()
        user.email = email
        user.set_password(password)
        try:
            user.save()
            return user
        except (ValueError, IntegrityError):
            pass
