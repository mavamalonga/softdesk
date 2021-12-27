from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from app import models, serializers

class ProjectViewset(ModelViewSet):
	serializer_class = serializers.ProjectSerializer

	def get_queryset(self):
		return models.Projects.objects.all()