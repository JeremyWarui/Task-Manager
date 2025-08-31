from django.shortcuts import render

# Create your views here.
def index(request):
    """
    The function that handles the view for the root page
    :param request:
    :return: html doc
    """
    return render(request, "tasks/index.html")