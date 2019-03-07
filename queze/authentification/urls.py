from django.urls import path

from authentification.views import registration, log_in

urlpatterns = [
    path('registration', registration),
    path('login', log_in)
]