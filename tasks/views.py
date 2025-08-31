from django.shortcuts import render, get_object_or_404
from .models import Task

# Create your views here.
def index(request):
    """
    The function that handles the view for the root page
    :param request:
    :return: html doc
    """
    return render(request, "tasks/base.html")


def task_list(request):
    tasks = Task.objects.all().order_by('created_at')
    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task })


