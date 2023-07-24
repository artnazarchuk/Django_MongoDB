from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Customer
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
        string_created = f'Ордер заказчика под ID №{instance.CustomerId} с именем: {instance.CustomerName}, добален'
        server_logs(string_created)
    else:
        string_update = f'Ордер заказчика под ID №{instance.CustomerId} с именем: {instance.CustomerName}, редактирован'
        server_logs(string_update)

@receiver(post_delete, sender=Customer)
def post_delete_order(origin, **kwargs):
    print(kwargs)
    string_delete = f'Ордер заказчика под ID №{origin.CustomerId} с именем: {origin.CustomerName}, удалён'
    server_logs(string_delete)
