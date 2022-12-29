from django.urls import path, re_path

from . import views

urlpatterns = [
    path('department/', views.departments_all),
    path('ward/', views.wards_all),
]