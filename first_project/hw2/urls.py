from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.main),
    path('main/', views.main),
    path('news/', views.news),
    path('facts/', views.facts),
    path('contacts/', views.contacts),
    path('history/', views.history_total),
    path('history/<str:parameter>/', views.history),
    path('management/', views.management),
    re_path('main/\w*', views.main),
    re_path('news/\w*', views.news),
    re_path('facts/\w*', views.facts),
    re_path('contacts/\w*', views.contacts),
    re_path('management/\w*', views.management),
]
