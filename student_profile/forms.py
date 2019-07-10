from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    """
    """
    class Meta:
        model=Profile
        fields=('student_name','reg_no','course','year_of_study','about','avatar')
        