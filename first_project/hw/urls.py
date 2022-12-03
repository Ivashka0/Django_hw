from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index),
    path('hw/sec/<str:name>/', views.main),
    path('hw/check/<int:number>/', views.check),
    path('hw/find/<str:name>/<str:password>/', views.connect),
    re_path(r'^hw/email/(?P<email>[\w]+@([\w-]+\.)+[\w-]{2,4})/$', views.email_resp),
    re_path(r'^hw/phone/(?P<phone>\+[\d]{12})/$', views.phone_resp),
]