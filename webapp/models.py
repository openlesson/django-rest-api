from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    choices = (('H', 'HIGH'), ('M', 'MEDIUM'), ('L', 'LOW'))
    priority = models.CharField(max_length=1, choices=choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
