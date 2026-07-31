from django.db import models

from .author_model import Author
from .editorial_model import Editorial


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, null=True, blank=False, unique=True)
    publication_date = models.DateField(null=True, blank=True)
    pages_number = models.PositiveIntegerField()

    LANGS_CHOICES = {
        'ES':'Español',
        'EN': 'Inglés',
    }

    language = models.CharField(max_length=20, choices=LANGS_CHOICES, default='ES')
    description = models.TextField(null=True, blank=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2 ,null=True, blank=True)
    is_out_of_stock = models.BooleanField(default=False)
    authores = models.ManyToManyField(
        Author,
        through='BookAuthor',
        related_name='books', # esta parametro sera utilizado por el modelo Author como nombre de relacion con el modelo Books ejem: author.books.filter()
    )

    def __str__(self):
        return f'title: {self.title},isbn: {self.isbn} editorial{self.editorial}, autor(es){self.authores}'
    
