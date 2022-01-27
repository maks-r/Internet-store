from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(verbose_name="аватар", blank=True, upload_to="users")
    age = models.PositiveIntegerField(verbose_name="возраст")
    phone = models.CharField(verbose_name="телефон", max_length=20, blank=True)
    city = models.CharField(verbose_name="город", max_length=30, blank=True)