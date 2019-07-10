from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.homepage, name='homepage'),
    url('^create_profile', views.create_profile, name='create_profile'),
    
    
]