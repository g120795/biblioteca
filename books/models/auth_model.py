from django.db import models

class Auth(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    born = models.DateField()
    nationality = models.CharField(max_length=100)
    biograpy = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank=True, null= True)
    web_site = models.URLField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'nombre: {self.name}'

    

