from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from todolist.forms import TaskForm
from django.core.paginator import Paginator


@login_required
def todolist(request):
    if request.method == "POST":
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            task = form_data.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully')
        return redirect('todolist')

    filter_status = request.GET.get('status', 'all')
    tasks_qs = Task.objects.filter(user=request.user).order_by('id')

    if filter_status == 'completed':
        tasks_qs = tasks_qs.filter(is_completed=True)
    elif filter_status == 'pending':
        tasks_qs = tasks_qs.filter(is_completed=False)

    completed_count = Task.objects.filter(user=request.user, is_completed=True).count()
    pending_count = Task.objects.filter(user=request.user, is_completed=False).count()

    paginator = Paginator(tasks_qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todolist.html', {
        'page_obj': page_obj,
        'completed_count': completed_count,
        'pending_count': pending_count,
        'current_filter': filter_status,
    })


@login_required
def homepage(request):
    return render(request, 'main.html', {})


@login_required
def contact(request):
    return render(request, 'contact.html', {})


@login_required
def about(request):
    return render(request, 'about.html', {})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.error(request, 'Task deleted successfully')
    return redirect('todolist')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        form_data = TaskForm(request.POST, instance=task)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Task updated successfully')
    return redirect('todolist')


@login_required
def complete_task(request, task_id):
    task_obj = get_object_or_404(Task, id=task_id, user=request.user)
    task_obj.is_completed = True
    task_obj.save()
    messages.success(request, "Task completed!")
    return redirect("todolist")


@login_required
def pending_task(request, task_id):
    task_obj = get_object_or_404(Task, id=task_id, user=request.user)
    task_obj.is_completed = False
    task_obj.save()
    messages.success(request, "Task Pending.")
    return redirect("todolist")
