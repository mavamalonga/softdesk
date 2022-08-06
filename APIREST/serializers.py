from rest_framework.serializers import ModelSerializer, SerializerMethodField
from APIREST import models 


class ProjectSerializer(ModelSerializer):
	issues = SerializerMethodField()

	class Meta:
		model = models.Project
		fields = ['id', 'title', 'description', 'tag', 'author', 'contributors', 'issues']

	def get_issues(self, instance):
		queryset = models.Issue.objects.filter(project_id=instance.id)
		serializer = IssueSerializer(queryset, many=True)
		return serializer.data


class IssueSerializer(ModelSerializer):
	comments = SerializerMethodField()

	class Meta:
		model = models.Issue
		fields = ['id', 'title', 'author', 'description', 'project', 'created_time', 'comments']

	def get_comments(self, instance):
		queryset = models.Comment.objects.filter(issue_id=instance.id)
		serializer = CommentSerializer(queryset, many=True)
		return serializer.data


class CommentSerializer(ModelSerializer):

	class Meta:
		model = models.Comment
		fields = "__all__"
