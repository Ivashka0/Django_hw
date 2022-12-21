from django.urls import path, re_path

from . import views

urlpatterns = [
    path('dictsort/', views.dictsort),
    path('dictsort1/', views.pri),
    path('dictsort2/', views.pra),
    path('dictsort3/', views.pre)
]