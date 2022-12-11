from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.main),
    path('main/', views.main),
    path('facts/', views.facts),
    path('cities/', views.cities),
    path('cities/<str:name_city>/', views.city),
    path('cities/<str:name_city>/<int:year>/', views.city_data),
    path('history/', views.history_total),
    path('history/<int:date>/', views.history),
    re_path('main/\w*', views.main),
    re_path('facts/\w*', views.facts),
    re_path('cities/<str:name_city>/<int:year>^[0-9]/', views.city_data),
    re_path('history/<int:date>^[0-9]/', views.history),
    re_path('cities/\w*', views.cities),
    re_path('history/\w*', views.history_total),
]
