# -*- coding=utf8 -*-
from django.db import models
# Create your models here.
class testMan(models.Model):
    name=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    adress=models.CharField(max_length=30)
    