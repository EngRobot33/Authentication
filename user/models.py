from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, verbose_name='active')

    def __str__(self):
        return f'User: {self.user.username}'
