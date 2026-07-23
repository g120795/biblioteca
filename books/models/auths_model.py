from django.db import models
from book_model import Book
from auth_model import Auth

class Auths(models.Model):
    auth = models.ForeignKey(Auth, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL)