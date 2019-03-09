from django.urls import path

from authentification.views import registration, log_in, log_out, delete_user, get_user, update_user

urlpatterns = [
    path('registration', registration),
    path('login', log_in),
    path('logout', log_out),
    path('delete_user/<int:user_id>', delete_user),
    path('get_user/<int:user_id>', get_user),
    path('update_user/<int:user_id>', update_user)
]