from django.db import models
from .auth_model import Auth
from .editorial_model import Editorial

class Book(models.Model):
    title = models.CharField(max_length=200)
    auth = models.ForeignKey(Auth, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=20, null=True, blank=False)
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

    def __str__(self):
        return f'title: {self.title}'
    
