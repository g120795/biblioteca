from django.urls import path
from ..views.editorials_views import list_editorials

urlpatterns = [
    path('list_editorials/', list_editorials, name='list_editorials')
]