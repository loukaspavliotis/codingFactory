from django.apps import AppConfig


# class AppConfig(AppConfig):
#     name = 'app'
#
#
# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.user.username
#
#
from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        # If you need to perform specific actions when the app is ready,
        # you can include that logic here (e.g., signals or imports).
        pass