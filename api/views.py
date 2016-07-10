from django.shortcuts import render, HttpResponse
from serializers import PeopleSerializer
from rest_framework import viewsets

# Only 1 view

def index(request):
	return render(request,'index.html')
	

