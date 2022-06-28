from django.conf import settings
from django.db import models
from django.contrib.auth.models import UserManager,AbstractUser,User


class UserInformation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    birth = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user




