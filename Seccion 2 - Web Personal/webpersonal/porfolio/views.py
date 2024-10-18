from django.shortcuts import render
from .models import Project

# Create your views here.
def porfolio(request):
    # projects = Project.objects.all()
    # return render(request=request, template_name="porfolio/porfolio.html", {'projects': projects})
    return render(request=request, template_name="porfolio/porfolio.html")
