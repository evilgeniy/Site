from django.apps import AppConfig
from django.contrib.auth import default_app_config


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
