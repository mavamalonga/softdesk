from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from app import models 

class ProjectSerializer(ModelSerializer):

	issues = SerializerMethodField()

	class Meta:
		model = models.Project
		fields = ['id', 'title', 'description', 'projet_type', 'issues']

	def get_issues(self, instance):
		queryset = models.Issue.objects.filter(project_id=instance.id)
		serializer = IssueSerializer(queryset, many=True)
		return serializer.data

class ProjectDetailSerializer(ModelSerializer):

	class Meta:
		model = models.Project
		fields = ['id', 'title', 'description', 'projet_type']

class IssueSerializer(ModelSerializer):

	class Meta:
		model = models.Issue
		fields = ['title', 'description', 'tag', 'priority', 'status', 'assignee_user_id', 'created_time']