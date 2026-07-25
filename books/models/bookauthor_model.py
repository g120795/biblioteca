from django.db import models

from .author_model import Author
from .book_model import Book


class BookAuthor(models.Model):
    auth = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)