from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def projects(request):
    # return HttpResponse('Here are the products')
    return render(request, 'projects/projects.html')

def project(request, pk):
    # return HttpResponse('Here is the product')
    return render(request, 'projects/single-project.html')
