from django.db import models

# Create your models here.
class TypeService(models.Model):
    ServiceId = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=100)
    ServiceFile = models.FileField(upload_to='')

class Customer(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=50)
    CustomerEmail = models.EmailField(max_length=50)  # unique=True
    CustomerPhone = models.CharField(max_length=30)
    CustomerCar = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
