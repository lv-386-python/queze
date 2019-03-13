from django.urls import path

import poll.views as test

urlpatterns = [
    path('get_test/<int:test_id>', test.get_test),
    path('create_test', test.create_test),
    path('update_test/<int:test_id>', test.update_test),
    path('delete_test/<int:test_id>', test.delete_test),
]
