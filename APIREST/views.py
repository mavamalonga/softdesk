from statistics import mode
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from APIREST.permissions import IsContrubutorOrIsOwner
from APIREST import models


class ProjectViewset(ModelViewSet):
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return models.Project.objects.all()


class IssueViewset(ModelViewSet):
	permission_classes = [IsContrubutorOrIsOwner]

	def get_queryset(self):
		return models.Issue.objects.all()


class CommentViewset(ModelViewSet):
	permission_classes = [IsContrubutorOrIsOwner]

	def get_queryset(self):
		return models.Comment.objects.all()
