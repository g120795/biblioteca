from django.urls import path

from ..views.auth_views import (
    content_auth,
    create_author,
    detail_author,
    edit_author,
    read_authors,
)

urlpatterns = [
    path('content_auth/',content_auth, name='content_auth'),
    path('create_author/', create_author, name='create_author'),
    path('read_authors/', read_authors, name='read_authors'),
    path('<int:author_id>/edit_author/', edit_author, name='edit_author'),
    path('<int:author_id>/detail_author/', detail_author, name='detail_author')
]