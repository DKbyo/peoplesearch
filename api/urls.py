from django.conf.urls import url, include
from viewsets import  PeopleAllAPI, UploadAPI,PeopleAPI
from . import views

"""
URL mapping, we only have 1 page, all other urls are REST related

"""

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^people/upload/', UploadAPI.as_view()),	
    url(r'^people/all/', PeopleAllAPI.as_view()),    
    url(r'^people/', PeopleAPI.as_view()),    
]
