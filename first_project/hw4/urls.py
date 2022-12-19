from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.main),
    path('main/', views.main),
    path('writers/', views.writers),
    path('writers/<str:name_writer>/', views.writer),
    path('writers/<str:name>/<str:book>/', views.writers_book),
    path('books/', views.books),
    path('books/<int:place>/', views.book_top),
    re_path('main/\w*', views.main),
    re_path('writers/\w*', views.writers),
    re_path('books/\w*', views.books),
    re_path('books/<int:place>^[0-9]/', views.book_top),
]
