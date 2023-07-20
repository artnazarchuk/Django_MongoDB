from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ServiceApp.models import TypeService, Customer
from ServiceApp.serializers import TypeServiceSerializer, CustomerSerializer

# Create your views here.

@csrf_exempt
def TypeServiceApi(request, pk):
    if request.method == 'GET':
        typeservice = TypeService.objects.all()
        typeservice_serializer = TypeServiceSerializer(typeservice, many=True)
        return JsonResponse(typeservice_serializer.data, safe=False)
    elif request.method == 'POST':
        typeservice_data = JSONParser().parse(request)
        typeservice_serializer = TypeServiceSerializer(data=typeservice_data)
        if typeservice_serializer.is_valid():
            typeservice_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        typeservice_data = JSONParser().parse(request)
        typeservice = TypeService.objects.get(ServiceId=typeservice_data['ServiceId'])
        typeservice_serializer = TypeServiceSerializer(typeservice, data=typeservice_data)
        if typeservice_serializer.is_valid():
            typeservice_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        typeservice = TypeService.objects.get(ServiceId=pk)
        typeservice.delete()
        return JsonResponse('Deleted Successfully', safe=False)

