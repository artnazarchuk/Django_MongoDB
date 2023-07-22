from django.db import models

# Create your models here.
class TypeService(models.Model):
    ServiceId = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=100)
    ServiceFile = models.CharField(max_length=30, null=True)

class Customer(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=50)
    CustomerPhone = models.CharField(max_length=30)
    CustomerCar = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/{self.CustomerId}/update'

