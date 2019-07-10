from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_profile(request):
    """
    """
    current_user = request.user 
    if request.method =='POST':
        profile_form=ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            created_profile = form.save(commit=False)
            created_profile.user_id = current_user.id
            created_profile.save()
        return redirect(view_profile)
    else:
        profile_form=ProfileForm()
    return render(request, 'profile_form.html',{'profile_form':profile_form})
