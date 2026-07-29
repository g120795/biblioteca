from django.urls import path

from books.views.editorials_views import (
    content_editorials,
    create_editorial,
    delete_editorial,
    detail_editorial,
    edit_editorial,
    read_editorials,
)

urlpatterns = [
    path('content_editorials/', content_editorials, name='content_editorials'),
    path('create_editorial/', create_editorial, name= 'create_editorial'),
    path('read_editorials/', read_editorials, name='read_editorials'),
    path('<int:editorial_id>/detail_editorial/', detail_editorial, name='detail_editorial'),
    path('<int:editorial_id>/edit_editorial/', edit_editorial, name='edit_editorial'),
    path('<int:editorial_id>/delete_editorial/', delete_editorial, name='delete_editorial'),
]