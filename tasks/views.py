from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    """
    The function that handles the view for the root page
    :param request:
    :return: html doc
    """
    return render(request, "tasks/base.html")


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task })

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Task updated")
        return redirect('task_list')
    return render(request, "tasks/task_form.html", {'form': form })

def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        messages.success(request, "Task created!")
        return redirect("task_list")
    return render(request, "tasks/task_form.html", { 'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.info(request, 'Task deleted')
        return redirect('task_list')
    return render(request, "tasks/task_confirm_delete.html", { 'task': task})