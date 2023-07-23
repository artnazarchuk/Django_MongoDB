from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Customer

@receiver(post_save, sender=Customer)
def post_create_update_order(created, **kwargs):
    instance = kwargs['instance']
    if created:
        print(f'Ордер заказчика под ID №{instance.CustomerId} с именем: {instance.CustomerName}, добален')
    else:
        print(f'Ордер заказчика под ID №{instance.CustomerId} с именем: {instance.CustomerName}, редактирован')

@receiver(post_delete, sender=Customer)
def post_delete_order(origin, **kwargs):
    print(f'Ордер заказчика под ID №{origin.CustomerId} с именем: {origin.CustomerName}, удалён')
