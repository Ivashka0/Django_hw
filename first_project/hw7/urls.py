from django.urls import path, re_path

from . import views

urlpatterns = [
    path('wards/', views.wards_all),
    path('doctors/', views.doctors_all),
    path('diseases/', views.diseases_all),
    path('departments/', views.departments_all),
    path('examinations/', views.examinations_all),
]