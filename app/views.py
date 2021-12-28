from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app import models, serializers

class Project_list(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		projects = models.Project.objects.all()
		serializer = serializers.ProjectSerializer(projects, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = serializers.ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(author_user_id=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Project_detail(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, pk):
		try:
			project = models.Project.objects.get(pk=pk)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = serializers.ProjectDetailSerializer(project)
		return Response(serializer.data)

	def put(self, request, format=None):
		serializer = serializers.ProjectSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		project.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class Issue_list(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request):
		issues = models.Issue.objects.all()
		serializer = serializers.IssueSerializer(issues, many=True)
		return Response(serializer.data)


