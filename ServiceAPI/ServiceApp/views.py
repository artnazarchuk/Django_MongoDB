from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from django.views.generic import UpdateView, DeleteView

from ServiceApp.models import TypeService, Customer
from ServiceApp.serializers import TypeServiceSerializer, CustomerSerializer
from .form import CustomerModelForm

# Create your views here.

# CRUD для TypeService
@csrf_exempt
def TypeServiceApi(request, pk=0):
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
        typeservice_data['ServiceFile'] = typeservice.ServiceFile
        # ServiceId=typeservice_data['ServiceId'] - нужно указывать ServiceId в запросе
        # ServiceId=pk - нужно указывать ServiceId в URL
        typeservice_serializer = TypeServiceSerializer(typeservice, data=typeservice_data)
        if typeservice_serializer.is_valid():
            typeservice_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        try:
            typeservice = TypeService.objects.get(ServiceId=pk)
        except:
            return JsonResponse('Object does not exists', safe=False)
        typeservice.delete()
        return JsonResponse('Deleted Successfully', safe=False)

# CRUD для Customer
@csrf_exempt
def CustomerApi(request, pk=0):
    if request.method == 'GET':
        customer = Customer.objects.all()
        customer_serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        print(customer_data)
        customer_serializer = CustomerSerializer(data=customer_data)
        print(customer_serializer.is_valid())
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer = Customer.objects.get(CustomerId=pk)
        # CustomerId=customer_data['ServiceId'] - нужно указывать CustomerId в запросе
        # CustomerId=pk - нужно указывать ServiceId в URL
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        print(customer_serializer)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        try:
            customer = Customer.objects.get(CustomerId=pk)
        except:
            return JsonResponse('Object does not exists', safe=False)
        customer.delete()
        return JsonResponse('Deleted Successfully', safe=False)

@csrf_exempt
def SaveFile(request, pk):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    typeservice = TypeService.objects.get(ServiceId=pk)
    print(typeservice)
    typeservice_data = {'ServiceId': pk, 'ServiceName': typeservice.ServiceName, 'ServiceFile': file_name}
    typeservice_serializer = TypeServiceSerializer(typeservice, data=typeservice_data)
    if typeservice_serializer.is_valid():
        typeservice_serializer.save()
    return JsonResponse(file_name, safe=False)

def index(request):
    typeservice = TypeService.objects.all()
    return render(request, 'ServiceApp/index.html', {'title': 'Главная страница', 'service': typeservice})

def customer_orders(request):
    customer = Customer.objects.all()
    return render(request, 'ServiceApp/customer_orders.html', {'title': 'Заявки клиентов', 'customer_order': customer})

def create_order(request):
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            task = Customer(
                CustomerName=form.cleaned_data['CustomerName'],
                CustomerPhone=form.cleaned_data['CustomerPhone'],
                CustomerCar=form.cleaned_data['CustomerCar'],
            )
            task.save()
            return redirect('orders')

    context = {
        'form': form,
    }
    print(context)
    return render(request, 'ServiceApp/create_order.html', context)

class CustomerUpdateApi(UpdateView):
    form_class = CustomerModelForm
    model = Customer
    template_name = 'ServiceApp/update_order.html'

class CustomerDeleteApi(DeleteView):
    model = Customer
    success_url = '/customer_orders'
