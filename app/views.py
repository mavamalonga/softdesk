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

	permission_classes = [permissions.IsContrubutorAndOwner]

	def get(self, request, project_id):
		project = get_object_or_404(models.Project, pk=project_id)
		contributors = models.Contributor.objects.filter(project_id=project_id)
		contributor = get_object_or_404(contributors, user=request.user.id)
		self.check_object_permissions(self.request, contributor)
		serializer = serializers.ProjectDetailSerializer(project)
		return Response(serializer.data)

	def put(self, request, project_id):
		project = get_object_or_404(models.Project, pk=project_id)
		self.check_object_permissions(self.request, project)
		serializer = serializers.ProjectViewPostSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, project_id):
		project = get_object_or_404(models.Project, pk=project_id)
		self.check_object_permissions(self.request, project)
		content = {"respose": f"project {project.title} deleted"}
		project.delete()
		return Response(content)


class ContributorView(APIView):

	permission_classes = [permissions.IsContrubutorAndOwner]

	def get(self, request, project_id):
		project = get_object_or_404(models.Project, pk=project_id)
		contributors = models.Contributor.objects.filter(project_id=project_id)
		contributor = get_object_or_404(contributors, user=request.user.id)
		self.check_object_permissions(self.request, contributor)
		serializer = serializers.ContributorGetSerializer(contributors, many=True)
		return Response(serializer.data)
	
	def post(self, request, project_id):
		project = get_object_or_404(models.Project, pk=project_id)
		self.check_object_permissions(self.request, project)
		serializer = serializers.ContributorAddSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(project_id=project.id)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, project_id):
		project = get_object_or_404(models.Project, pk=project_id)
		self.check_object_permissions(self.request, project)
		contributor = models.Contributor.objects.filter(project_id=project_id).get(
				user=request.data['user'])
		contributor.delete()
		content = {"response": f"contributor {request.data['user']} deleted"}
		return Response(content)


class IssueView(APIView):

	permission_classes = [permissions.IsContrubutorAndOwner]

	def get(self, request, project_id):
		project = get_object_or_404(models.Project, pk=project_id)
		contributors = models.Contributor.objects.filter(project_id=project_id)
		contributor = get_object_or_404(contributors, user=request.user.id)
		self.check_object_permissions(self.request, contributor)
		issues = models.Issue.objects.filter(project_id=project_id)
		if issues.count() == 0:
			return Response({"response":"the issues list is empty "})
		serializer = serializers.IssueSerializer(issues, many=True)
		return Response(serializer.data)

	def post(self, request, project_id):
		project = get_object_or_404(models.Project, pk=project_id)
		contributors = models.Contributor.objects.filter(project_id=project_id)
		contributor = get_object_or_404(contributors, user=request.user.id)
		self.check_object_permissions(self.request, contributor)
		serializer = serializers.IssuePostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(project_id=project_id, author=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueDetail(APIView):

	permission_classes = [permissions.IsContrubutorAndOwner]

	def put(self, request, project_id, issue_id):
		issue = get_object_or_404(models.Issue, pk=issue_id)
		self.check_object_permissions(self.request, issue)
		serializer = serializers.IssuePostSerializer(issue, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, project_id, issue_id):
		issue = get_object_or_404(models.Issue, pk=issue_id)
		self.check_object_permissions(self.request, issue)
		issue.delete()
		content = {"response":"issue deleted"}
		return Response(content)


class Comment(APIView):

	permission_classes = [permissions.IsContrubutorAndOwner]

	def get(self, request, project_id, issue_id):
		contributors = models.Contributor.objects.filter(project_id=project_id)
		contributor = get_object_or_404(contributors, user=request.user.id)
		self.check_object_permissions(self.request, contributor)
		comments = models.Comment.objects.filter(issue=issue_id)
		if comments.count() == 0:
			return Response({"response":"the comments list is empty "})
		serializer = serializers.CommentSerializer(comments, many=True)
		return Response(serializer.data)

	def post(self, request, project_id, issue_id):
		project = get_object_or_404(models.Project, pk=project_id)
		contributors = models.Contributor.objects.filter(project_id=project_id)
		contributor = get_object_or_404(contributors, user=request.user.id)
		self.check_object_permissions(self.request, contributor)
		issues = models.Issue.objects.filter(project_id=project_id)
		issue = get_object_or_404(issues, pk=issue_id)
		serializer = serializers.CommentPostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(issue=issue, author=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

	permission_classes = [permissions.IsContrubutorAndOwner]

	def get(self, request, project_id, issue_id, comment_id):
		project = get_object_or_404(models.Project, pk=project_id)
		contributors = models.Contributor.objects.filter(project_id=project_id)
		contributor = get_object_or_404(contributors, user=request.user.id)
		self.check_object_permissions(self.request, contributor)
		comment =  get_object_or_404(models.Comment, pk=comment_id)
		serializer = serializers.CommentSerializer(comment)
		return Response(serializer.data)

	def put(self, request, project_id, issue_id, comment_id):
		comment = get_object_or_404(models.Comment, pk=comment_id)
		self.check_object_permissions(self.request, comment)
		serializer = serializers.CommentPostSerializer(comment, data=request.data)
		if serializer.is_valid():
			serializer.save(issue=issue, author=request.user)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, project_id, issue_id, comment_id):
		comment = get_object_or_404(models.Comment, pk=comment_id)
		self.check_object_permissions(self.request, comment)
		comment.delete()
		content = {"response":"comment deleted"}
		return Response(content)

