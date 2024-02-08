from django.apps import AppConfig


class CustomModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_model'
