from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    ref = models.CharField(max_length=8)
    cost = models.FloatField()
    price = models.FloatField()
    
    def __str__(self):
        return str(self.id)

