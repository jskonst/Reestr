# -*- coding=utf8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager
# Create your models here.
class CustomUser(User):
    timezone = models.CharField(max_length=50, default='Europe/London')
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()