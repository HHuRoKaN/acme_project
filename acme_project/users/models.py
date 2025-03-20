from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthday_date = models.DateField(null=True)
    bio = models.TextField(null=True)
