# network/models.py
from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,) # The method must return a tuple