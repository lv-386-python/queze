from django.urls import path

import Tests.views as test_views

urlpatterns = [
    path('get_test/<int:test_id>', test_views.get_test),
    path('create_test', test_views.create_test),
    path('update_test/<int:test_id>', test_views.update_test),
    path('delete_test/<int:test_id>', test_views.delete_test),
    path('create_question', test_views.create_question),
    path('update_question/<int:question_id>', test_views.update_question),
    path('delete_question/<int:question_id>', test_views.delete_question),
    path('get_question/<int:question_id>', test_views.get_question),
    path('get_results/<int:results_id>', test_views.get_results),
    path('create_user_answer', test_views.create_user_answer),
    path('get_user_answer/<int:user_answer_id>', test_views.get_user_answer),
    path('update_user_answer/<int:user_answer_id>', test_views.update_user_answer)
]
