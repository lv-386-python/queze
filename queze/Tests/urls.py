from django.urls import path

from Tests.views import create_test

urlpatterns = [
    path('create', create_test),
]
