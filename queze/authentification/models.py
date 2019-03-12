from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import IntegrityError


# Create your models here.
from django.forms import model_to_dict


class CustomUser(AbstractBaseUser):
    '''
    User django model
    '''
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    object = BaseUserManager()

    @staticmethod
    def create(email, password):
        '''method for creating new user in database'''
        user = CustomUser()
        user.email = email
        user.set_password(password)
        try:
            user.save()
            return user
        except (ValueError, IntegrityError):
            pass

    @staticmethod
    def delete_by_id(user_id):
        '''method for deleting user from database'''
        try:
            user = CustomUser.object.get(id=user_id)
            user.delete()
        except ObjectDoesNotExist:
            print('not found')
        return True

    @staticmethod
    def get_user(user_id):
        '''method for getting user from database'''
        try:
            user = CustomUser.object.get(id=user_id)
        except ObjectDoesNotExist:
            return False
        return model_to_dict(user)

    @staticmethod
    def update_user(user_id, data):
        '''method for updating user in database'''
        try:
            user = CustomUser.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return False
        user.email = data['new_email']
        user.password = data['new_password']
        try:
            user.save()
            return True
        except:
            return False
