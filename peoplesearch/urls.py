"""peoplesearch URL Configuration

API A visual api for quick search
admin Django standard admin site

"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [ 
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
]
