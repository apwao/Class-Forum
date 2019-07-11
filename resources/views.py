from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
# from .forms import ProfileForm
# from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    """
    """
    
    return render(request, 'homepage.html')

def create_profile(request):
    """
    """
    return render(request, 'profile_form.html')
