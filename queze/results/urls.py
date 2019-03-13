from django.urls import path

import results.views as results_views

urlpatterns = [
    path('get_result/<int:results_id>', results_views.get_result),
]
