from django.urls import path

from ..views.auth_views import content_auth, create_author

urlpatterns = [
    path('content_auth/',content_auth, name='content_auth'),
    path('create_author/', create_author, name='create_author'),
]