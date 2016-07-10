import django_filters
from models import People
from serializers import PeopleSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import filters
from rest_framework import generics
"""
REST API Views

"""

class PeopleFilter(filters.FilterSet):
	query = django_filters.CharFilter(name="query")
	class Meta:
	        model = People
		fields = ('id','name','last_name')


class PeopleAPI(generics.ListAPIView):
	queryset = People.objects.all()
	serializer_class = PeopleSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'last_name')

class PeopleAllAPI(APIView):
	def delete(self,request):
		People.objects.all().delete()
	

class UploadAPI(APIView):
	parser_classes = (FileUploadParser,)
	
	def post(self,request,filename=None, format=None):
		uploadedFile = request.data['file']
		for line in uploadedFile:
			data = line.split(',')
			newPeople = People(id=data[0],name=data[1],last_name=data[2])		
			newPeople.save()	
			print line
		return Response(status=204)


