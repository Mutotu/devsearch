from email.mime import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


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


@login_required(login_url="login")
def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        # see if all the fields are checked
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,  instance=project)
        # see if all the fields are checked
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'object':object}
    return render(request, 'projects/delete_template.html', context)