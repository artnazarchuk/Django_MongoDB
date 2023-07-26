from django.db.models.signals import post_save, post_delete, pre_save
from django.core.signals import request_started, request_finished
from django.core.handlers.wsgi import WSGIHandler
from django.dispatch import receiver, Signal
from .models import Customer, TypeService
import datetime

def server_logs(string):
    with open('server_logs.txt', 'a', encoding='utf-8') as file:
        now = str(datetime.datetime.now())
        string = f'# {now} {string}'
        print(string)
        file.write(string + '\n')

@receiver(post_save, sender=Customer)
def post_create_update_order(created, **kwargs):
    instance = kwargs['instance']
    if created:
        string_created = f'Ордер заказчика под ID №: {instance.CustomerId} с именем: {instance.CustomerName}, добален'
        server_logs(string_created)
    else:
        string_update = f'Ордер заказчика под ID №: {instance.CustomerId} с именем: {instance.CustomerName}, ' \
                        f'редактирован'
        server_logs(string_update)

@receiver(post_delete, sender=Customer)
def post_delete_order(origin, **kwargs):
    print(kwargs)
    string_delete = f'Ордер заказчика под ID №: {origin.CustomerId} с именем: {origin.CustomerName}, удалён'
    server_logs(string_delete)

@receiver(post_save, sender=TypeService)
def post_create_update_service(created, **kwargs):
    instance = kwargs['instance']
    if created:
        string_created = f'Сервис под ID №: {instance.ServiceId} с именем: {instance.ServiceName}, добален'
        server_logs(string_created)
    else:
        string_update = f'Сервис под ID №: {instance.ServiceId} с именем: {instance.ServiceName}, редактирован'
        server_logs(string_update)

@receiver(post_delete, sender=TypeService)
def post_delete_service(origin, **kwargs):
    print(f"ServiceName: {kwargs['instance'].ServiceName}")
    string_delete = f'Сервис под ID №: {origin.ServiceId} с именем: {origin.ServiceName}, удалён'
    server_logs(string_delete)

# @receiver(pre_save, sender=TypeService)
# def post_create_update_service_pre(using, **kwargs):
#     print(using)
#     print(kwargs)
#
# @receiver(request_started, sender=WSGIHandler)
# def request_service_api_start(environ, **kwargs):
#     print(environ)
#     print(kwargs['sender'])
#
# @receiver(request_finished, sender=WSGIHandler)
# def request_service_api_finish(**kwargs):
#     print(kwargs)

