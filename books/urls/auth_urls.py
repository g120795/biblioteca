from django.urls import path
from ..views.auth_views import list_auth
urlpatterns = [
    path('list_auth/', list_auth, name='list_auth')
]