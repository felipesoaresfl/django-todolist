from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloWorld(request):
    return HttpResponse('Hello World!')

def task_list(request):
    return render(request, 'tasks/list.html')

def yourname(request, name):
    context = {
        'name': name,
    }
    return render(request, 'tasks/yourname.html', context)