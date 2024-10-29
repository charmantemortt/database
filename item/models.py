from django.conf import settings
from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)