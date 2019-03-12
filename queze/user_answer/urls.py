from django.urls import path

import user_answer.views as user_answer_views

urlpatterns = [
    path('create', user_answer_views.create_user_answer),
    path('get_user_answer/<int:user_answer_id>', user_answer_views.get_user_answer),
    path('update_user_answer/<int:user_answer_id>', user_answer_views.update_user_answer)
]
