from email.mime import message
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm



def projects(request):
    # return HttpResponse('Here are the products')
    #####3
    # page = 'projects'
    # return render(request, 'projects/projects.html', {'page' : page} )
    ######
    # page = 'projects'
    # number= 101
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    # return HttpResponse('Here is the product')
    # projectObj = None
    # for i in projectsList:
    #     if i['id'] == pk:
    #         projectObj = i
    
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags':tags})

def create_project(request):
    form = ProjectForm()
    context = {'form':form}
    return render(request, "projects/project_form.html", context)