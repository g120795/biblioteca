from django.urls import path

from ..views.books_views import (
    content_books,
    create_book,
    delete_book,
    detail_book,
    edit_book,
    read_books,
)

urlpatterns = [
    path('content_books/', content_books, name='content_books'),
    path('create_book/', create_book, name='create_book'),
    path('read_books/', read_books, name='read_books'),
    path('<int:book_id>/edit_book/', edit_book, name='edit_book'),
    path('<int:book_id>/detail_book/', detail_book, name='detail_book'),
    path('<int:book_id>/delete_book/', delete_book, name='delete_book'),

]