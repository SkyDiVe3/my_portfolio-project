from django.shortcuts import render
from .models import Project
#This view method is called in urls.py file with keyname of home, it displays homepage
#
def home(request):
    # To call all objects with information from a model just call modelName.objects.all().
    #We store all objects from model Project to a variable:

    projects = Project.objects.all();
    return render(request, '../templates/portfolio/home.html', {'projects': projects})#To pass information to a template just type in brackets {'varName':keyVarName}
