from django.urls import path

import Tests.views as test_views

urlpatterns = [

    path('get_test/<int:test_id>', test_views.get_test),
    path('create_test', test_views.create_test),
    path('update_test/<int:test_id>', test_views.update_test),
    path('delete_test/<int:test_id>', test_views.delete_test),

]
