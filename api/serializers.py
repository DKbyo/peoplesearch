from models import People
from rest_framework.serializers import ModelSerializer
"""
REST Serializers
"""
class PeopleSerializer(ModelSerializer):
	class Meta:
		model = People
		fields = ('id','name','last_name')
