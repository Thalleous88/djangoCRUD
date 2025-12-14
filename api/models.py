from django.db import models

# Create your models here.
class Product(models.Model):
    data = models.JSONField(default=dict, blank=True)
    
