from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


# This part here is to use signal defined in signals.py file to automatically create user profile when creating a user
class MyAppConfig(AppConfig):
    name = 'project.api'

    def ready(self):
        User = get_user_model()
        from project.api.signals import create_profile
        post_save.connect(create_profile, sender=User)
