from django.db import models
from book_model import Book
from books.models.author_model import Auth

class BookAuthor(models.Model):
    auth = models.ForeignKey(Auth, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL)