from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=6)
    number=models.IntegerField()
    birth=models.DateField()
    password=models.CharField(max_length=20)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
