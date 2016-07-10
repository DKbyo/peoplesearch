"""peoplesearch URL Configuration

API A visual api for quick search
admin Django standard admin site

"""
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [ 
    url(r'^$', lambda r: HttpResponseRedirect('api/')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
]
