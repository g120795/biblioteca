from django.urls import path
from ..views.books_views import list_books, create_book
urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('create_book/', create_book, name='create_book')
]