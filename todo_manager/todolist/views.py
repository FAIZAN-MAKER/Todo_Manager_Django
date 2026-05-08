from django.shortcuts import render, redirect
from django.contrib import messages
from todolist.models import Task
from todolist.forms import TaskForm
# Create your views here.

def todolist(request):
    if request.method == "POST":
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Task added successfully')
        return redirect('todolist')
    all_tasks = Task.objects.all()
    return render(request, 'todolist.html', {'tasks': all_tasks})

def homepage(request):
    return render(request, 'main.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.error(request, 'Task deleted successfully')
    return redirect('todolist')