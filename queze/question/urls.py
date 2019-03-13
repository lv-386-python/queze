from django.urls import path

import poll.views as test_views

urlpatterns = [
    path('create', test_views.create_question),
    path('update/<int:question_id>', test_views.update_question),
    path('delete/<int:question_id>', test_views.delete_question),
    path('<int:question_id>', test_views.get_question),
]
