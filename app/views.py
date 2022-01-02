from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from app import models, serializers, permissions


class SignUpView(APIView):

	def post(self, request):
		serializer = serializers.SignUpSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectView(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request):
		projects = models.Project.objects.all()
		if projects.count() == 0:
			return Response({"response":"the project list is empty "})
		serializer = serializers.ProjectViewGetSerializer(projects, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = serializers.ProjectViewPostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(author=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectViewDetail(APIView):

	permission_classes = [permissions.ContributorOnly]

	def get(self, request, project_id):
		project = models.Project.objects.get(pk=project_id)
		serializer = serializers.ProjectDetailSerializer(project)
		return Response(serializer.data)

	def put(self, request, project_id):
		project = models.Project.objects.get(pk=project_id)
		serializer = serializers.ProjectViewPostSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		project = models.Project.objects.get(pk=pk)
		content = {"respose": "project {project.title} deleted"}
		project.delete()
		return Response(content)


class ContributorView(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id):
		contributors = models.Contributor.objects.filter(project_id=project_id)
		serializer = serializers.ContributorGetSerializer(contributors, many=True)
		return Response(serializer.data)
	
	def post(self, request, project_id):
		project = models.Project.objects.get(pk=project_id)
		serializer = serializers.ContributorAddSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(project_id=project.id)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, project_id):
		project = models.Project.objects.get(pk=project_id)
		contributor = models.Contributor.objects.filter(project_id=project_id).get(
				username=request.data['username'])
		contributor_deleted.delete()
		content = {"response": f"contributor {request.data['username']} deleted"}
		return Response(content)


class IssueView(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id):
		issues = models.Issue.objects.all()
		serializer = serializers.IssueSerializer(issues, many=True)
		return Response(serializer.data)

	def post(self, request, project_id):
		serializer = serializers.IssuePostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(project_id=project_id, author=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueDetail(APIView):

	permission_classes = [IsAuthenticated]

	def put(self, request, project_id, issue_id):
		serializer = serializers.IssuePostSerializer(issue, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, project_id, issue_id):
		issue = models.Issue.objects.filter(project_id=project_id).get(pk=issue_id)
		issue.delete()
		content = {"response":"issue deleted"}
		return Response(content)


class Comment(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id, issue_id):
		comments = models.Comment.objects.filter(issue=issue_id)
		serializer = serializers.CommentSerializer(comments, many=True)
		return Response(serializer.data)

	def post(self, request, project_id, issue_id):
		issue = models.Issue.objects.get(pk=issue_id)
		serializer = serializers.CommentPostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(issue=issue, author=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id, issue_id, comment_id):
		comment = models.Comment.objects.get(pk=comment_id)
		serializer = serializers.CommentSerializer(comment)
		return Response(serializer.data)

	def put(self, request, project_id, issue_id, comment_id):
		comment = models.Comment.objects.get(pk=comment_id)
		serializer = serializers.CommentPostSerializer(comment, data=request.data)
		if serializer.is_valid():
			serializer.save(issue=issue, author=request.user)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, project_id, issue_id, comment_id):
		comment = models.Comment.objects.get(pk=comment_id)
		comment.delete()
		content = {"response":"comment deleted"}
		return Response(content)

