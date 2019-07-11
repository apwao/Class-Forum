from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ProfileForm,NewProfileForm
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
            created_profile = profile_form.save(commit=False)
            created_profile.user_id = current_user
            created_profile.save()
        return redirect(view_profile)
    else:
        profile_form=ProfileForm()
    return render(request, 'profile_form.html',{'profile_form':profile_form})

def view_profile(request):
    """
    """
    current_user=request.user
    your_profile=Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'your_profile.html',{'your_profile':your_profile})

def edit_profile(request):
    """
    """
    current_user=request.user
    if request.method=='POST':
        user_profile=Profile.objects.get(user_id=current_user.id)
        form = NewProfileForm(request.POST)
        if form.is_valid():  
            new_form=form.save(commit=False)
            if new_form.get(student_name):
                new_name=new_form.get(student_name)
                user_profile.student_name = new_name
                user_profile.save_profile()
            if new_form.get(reg_no):
                new_reg_no=new_form.get(reg_no)
                user_profile.reg_no=new_reg_no
                user_profile.save_profile()
            if new_form.get(course):
                new_course=new_form.get(course)
                user_profile.course=new_course
                user_profile.save_profile()
            if new_form.get(about):
                new_about=new_form.get(about)
                user_profile.about=new_about
                user_profile.save_profile()
            form=NewProfileForm()
                
    else:
        form = NewProfileForm()
        
    return render(request, 'your_profile.html')
        
            
                
    
    