from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from app import models 

class ProjectSerializer(ModelSerializer):

	class Meta:
		model = models.Projects
		fields = ['id', 'title', 'description', 'projet_type']
