from django.urls import path
from ..views.books_views import list_books
urlpatterns = [
    path('list_books/', list_books, name='list_books')
]