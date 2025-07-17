from django.db import models
from home.models import Catalog

class Product(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
