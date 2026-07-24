from django.urls import path

from ..views.editorials_views import content_editorials, create_editorial

urlpatterns = [
    path('content_editorials/', content_editorials, name='content_editorials'),
    path('create_editorial/', create_editorial, name= 'create_editorial')
]