from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from app import models 

class ProjectSerializer(ModelSerializer):

	class Meta:
		model = models.Project
		fields = ['id', 'title', 'description', 'projet_type']