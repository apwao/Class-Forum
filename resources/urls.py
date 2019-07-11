from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.homepage, name='homepage'),
    url(r'^view_resources', views.view_resources, name='view_resources'),
    
]
