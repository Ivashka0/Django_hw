from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.product),
    path('<str:category>', views.products_filter),
    #path('from_cheapest', views.sort_cheapest)
]