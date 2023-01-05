from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.product),
    path('<str:category>/', views.products_filter),
    path('sorting/cheap/', views.sort_cheapest),
    path('sorting/expensive/', views.sort_expensive)
]