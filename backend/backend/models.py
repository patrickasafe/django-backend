from django.db import models

class Product(models.Model):
    name = models.CharField(max_lenght=200)
    description = models.CharField(max_length=500)