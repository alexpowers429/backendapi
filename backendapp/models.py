from django.db import models

# Create your models here.
class Car(models.Model):
    year = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)
    sellingFeatures = 

    def __str__(self):
        return f'{self.year}, {self.make}, {self.model}, {self.trim}, {self.sellingFeatures}'
