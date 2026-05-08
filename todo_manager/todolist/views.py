from django.shortcuts import render, redirect
from django.contrib import messages
from todolist.models import Task
from todolist.forms import TaskForm
from django.core.paginator import Paginator

# Create your views here.

def todolist(request):
    if request.method == "POST":
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Task added successfully')
        return redirect('todolist')

    filter_status = request.GET.get('status', 'all')
    tasks_qs = Task.objects.all().order_by('id')

    if filter_status == 'completed':
        tasks_qs = tasks_qs.filter(is_completed=True)
    elif filter_status == 'pending':
        tasks_qs = tasks_qs.filter(is_completed=False)

    completed_count = Task.objects.filter(is_completed=True).count()
    pending_count = Task.objects.filter(is_completed=False).count()

    paginator = Paginator(tasks_qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todolist.html', {
        'page_obj': page_obj,
        'completed_count': completed_count,
        'pending_count': pending_count,
        'current_filter': filter_status,
    })

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

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form_data = TaskForm(request.POST, instance=task)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Task updated successfully')
    return redirect('todolist')

def complete_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    task_obj.is_completed = True
    task_obj.save()
    messages.success(request, "Task completed!")
    return redirect("todolist")

def pending_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    task_obj.is_completed = False
    task_obj.save()
    messages.success(request, "Task Pending.")
    return redirect("todolist")
