from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    """task to be completed by team member(s)"""
    description = models.CharField(max_length = 200)
    deadline = models.CharField(max_length = 30)
    assigned_to = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.description