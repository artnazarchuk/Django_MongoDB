from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Customer, TypeService
from .tasks import add, add2, send_email_customer_create, send_email_customer_create1
from .tasks import send_email_customer_create2, send_email_customer_create3
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

        # вызываем тестовые методы
        add.delay(1, 10)
        add2.delay(1, 100)

        # вызываем метод отправки почты celery_tasks
        email = instance.CustomerEmail
        username = instance.CustomerName
        send_email_customer_create.delay(email, username)
        send_email_customer_create1.delay(email, username)
        send_email_customer_create2.delay(email, username)
        send_email_customer_create3.delay(email, username)
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
