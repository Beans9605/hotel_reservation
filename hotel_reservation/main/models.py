from django.db import models

# Create your models here.

class Reservation(models.Model) :
    reserve_date = models.DateField(auto_now=True)
    
    request_date = models.DateField(auto_now_add=True)
    
    user = models.CharField(max_length=10)





