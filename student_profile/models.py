from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    """
    Profile class to enable a student create their student profile
    """
    FRESHMAN='Freshman'
    SOPHOMORE='Sophomore'
    JUNIOR='Junior'
    SENIOR='Senior'
    YEAR_OF_STUDY_CHOICES=[
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    year_of_study=models.CharField(
        choices=YEAR_OF_STUDY_CHOICES,
        default=FRESHMAN,
        max_length=200,
    )
    student_name=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=300)
    course=models.CharField(max_length=200)
    about=HTMLField()
    avatar=models.ImageField()
    user_id=models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    
    
    def save_profile(self):
        """
        """
        self.save()
        
    def delete_profile(self):
        """
        """
        self.delete()
        
    def __str__(self):
        return self.student_name

        
        
