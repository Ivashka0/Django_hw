from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hw/sec/<str:name>/', views.main),
    path('hw/check/<int:number>/', views.check),
    path('hw/find/<str:name>/<str:password>/', views.connect),
]