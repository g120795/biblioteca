from django.urls import path

from ..views.books_views import content_books, create_book

urlpatterns = [
    path('content_books/', content_books, name='content_books'),
    path('create_book/', create_book, name='create_book')
]