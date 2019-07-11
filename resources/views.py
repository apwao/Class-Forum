from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ResourcesForm
from .models import Resources
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    """
    """
    
    return render(request, 'homepage.html')

def view_resources(request):
    """
    """
    resources=Resources.objects.all()
    return render(request, 'resources.html',{'resources':resources})
