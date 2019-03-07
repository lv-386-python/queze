from django.urls import path

from authentification.views import registration, log_in, log_out

urlpatterns = [
    path('registration', registration),
    path('login', log_in),
    path('logout', log_out)
]