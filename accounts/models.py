from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from minecraft.models import server

class CustomUser(AbstractUser):
    have_server = models.BooleanField(default=False)
    server = models.ForeignKey(server, on_delete=models.SET_NULL, null=True, blank=True)
