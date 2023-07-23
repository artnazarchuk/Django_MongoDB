from django.apps import AppConfig


class ServiceappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ServiceApp'

    def ready(self):
        from ServiceApp import signals
