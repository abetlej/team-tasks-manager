"""Defines URL patterns for team_tasks_managers"""

from django.conf.urls import url
from . import views

app_name = 'team_tasks_managers'
urlpatterns = [
    #home page
    url(r'^$', views.index, name = 'index'),
    #list of all tasks
    url(r'^tasks/$', views.tasks, name = 'tasks'),
    #certain task's page
    url(r'^task/(?P<task_id>\d+)/$', views.task, name = 'task'),
    #website used to add new task
    url(r'^new_task/$', views.new_task, name = 'new_task'),
    #save changes in completed tasks
    url(r'^cross_off/(?P<task_id>\d+)/$', views.cross_off, name = "cross_off"),
    url(r'^uncross/(?P<task_id>\d+)/$', views.uncross, name = "uncross"),
]