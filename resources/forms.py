from .models import Resources
from django import forms

class ResourcesForm(forms.ModelForm):
    """
    """
    class Meta:
        model:Resources
        fields=('topic','cover_image','resource_type','content','task')
        