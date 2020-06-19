from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    price=models.IntegerField()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
