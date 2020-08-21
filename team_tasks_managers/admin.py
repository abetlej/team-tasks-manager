from django.contrib import admin

# Register your models here.
from team_tasks_managers.models import Task

admin.site.register(Task)