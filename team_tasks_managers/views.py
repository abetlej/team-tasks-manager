from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    """Home page for Team Tasks Managers app"""
    return render(request, 'team_tasks_managers/index.html')

def tasks(request):
    """Displays all tasks"""
    tasks = Task.objects.filter(assigned_to=request.user).order_by('description')
    context = {'tasks': tasks}
    return render(request, 'team_tasks_managers/tasks.html', context)

@login_required
def task(request, task_id):
    """Displays given task"""
    task = Task.objects.get(id = task_id)
    if task.assigned_to != request.user:
        raise Http404
    context = {'task': task}
    return render(request, 'team_tasks_managers/task.html', context)

@login_required
def new_task(request):
    """Add new topic"""
    if request.method != 'POST':
        #No data passed, need to create a new form
        form = TaskForm()
    else:
        #data given using POST, need to store them
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit = False)
            new_task.assigned_to = request.user
            new_task.save()
            return HttpResponseRedirect(reverse('team_tasks_managers:tasks'))
    
    context = {'form': form}
    return render(request, 'team_tasks_managers/new_task.html', context)

def cross_off(request, task_id):
    task = Task.objects.get(id = task_id)
    task.completed = True
    task.save()
    tasks = Task.objects.filter(assigned_to=request.user).order_by('description')
    context = {'tasks': tasks}
    return render(request, 'team_tasks_managers/tasks.html', context)

def uncross(request, task_id):
    task = Task.objects.get(id = task_id)
    task.completed = False
    task.save()
    tasks = Task.objects.filter(assigned_to=request.user).order_by('description')
    context = {'tasks': tasks}
    return render(request, 'team_tasks_managers/tasks.html', context)