from django.db import models
from .book_model import Book
from .author_model import Author

class BookAuthor(models.Model):
    auth = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)