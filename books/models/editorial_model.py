from django.db import models
from django.contrib.auth.models import User

class Editorial(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=300)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank= True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    web_site = models.URLField(blank=True, null=True)
    year_foundation = models.DateField()
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    