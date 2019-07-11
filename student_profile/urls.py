from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.homepage, name='homepage'),
    url(r'^create_profile', views.create_profile, name='create_profile'),
    url(r'^view_profile',views.view_profile,name='view_profile'),
    url(r'^edit_profile',views.edit_profile, name='edit_profile'),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)