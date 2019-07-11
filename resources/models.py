from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Resources(models.Model):
    """
    class Resources to enable a admin to display resources in a class
    """
    Book='Book'
    Notes='Notes'
    Slides='Slides'
    Video='Video'
    Resource_choices=[
        (Book, 'Book'),
        (Notes, 'Notes'),
        (Slides, 'Slides'),
        (Video, 'Video'),
    ]
    
    Assignment='Assignment'
    Tutorial='Tutorial'
    Cat='Cat'
    Performance_results='Performance_results'
    Task_choices=[
        (Assignment, 'Assignment'),
        (Tutorial, 'Tutorial'),
        (Cat, 'Cat'),
        (Performance_results, 'Performance_results')
    ]
    
    cover_image=models.ImageField(upload_to='cover_photos/')
    topic=models.CharField(max_length=200)
    resource_type=models.CharField(
        choices=Resource_choices,
        default=Book,
        max_length=200,
    )
    posted_on=models.DateTimeField(auto_now_add=True)
    content=models.FileField(upload_to='resources/')
    task=models.CharField(
        choices=Task_choices,
        default=Notes,
        max_length=500,    
    )
    
  
    def save_resource(self):
        """
        """
        self.save()
        
    def delete_resource(self):
        """
        """
        self.delete()