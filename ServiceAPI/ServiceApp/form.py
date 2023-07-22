from .models import Customer
from django.forms import ModelForm, TextInput
from django import forms

class CustomerModelForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['CustomerName', 'CustomerPhone', 'CustomerCar']
        widgets = {
            'CustomerName': TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'Введите ваше имя'
            }),
            'CustomerPhone': TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'Введите номер телефона'
            }),
            'CustomerCar': TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'Введите название вашего автомобиля'
            }),
        }
