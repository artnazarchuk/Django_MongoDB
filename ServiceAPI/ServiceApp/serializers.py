from rest_framework import serializers
from ServiceApp.models import TypeService, Customer

class TypeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeService
        fields = ('ServiceId', 'ServiceName', 'ServiceFile')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('CustomerId', 'CustomerName', 'CustomerEmail', 'CustomerPhone', 'CustomerCar', 'time_create',
                  'time_update')
