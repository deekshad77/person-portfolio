from django.shortcuts import render
from . import models

def homepage(request):
    Projects= models.Project.objects.all()
    return render(request, 'portfol/home.html', {'projects':Projects})
