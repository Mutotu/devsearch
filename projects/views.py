from email.mime import message
from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    # return HttpResponse('Here are the products')
    #####3
    # page = 'projects'
    # return render(request, 'projects/projects.html', {'page' : page} )
    ######
    page = 'projects'
    number= 101
    context = {'page':page, 'number':number,'projects':projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    # return HttpResponse('Here is the product')
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
