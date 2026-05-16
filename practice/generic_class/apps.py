from django.apps import AppConfig


class GenericClassConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'generic_class'
