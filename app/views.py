from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#from app.permissions import IsAuthorOrReadOnly

from app import models, serializers

class SignUp(APIView):

	def post(self, request):
		serializer = serializers.SignUpSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		projects = models.Project.objects.all()
		serializer = serializers.ProjectSerializer(projects, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = serializers.ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(author=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, pk):
		try:
			project = models.Project.objects.get(pk=pk)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = serializers.ProjectDetailSerializer(project)
		return Response(serializer.data)

	def put(self, request, pk):
		try:
			project = models.Project.objects.get(pk=pk)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = serializers.ProjectSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		try:
			project = models.Project.objects.get(pk=pk)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)
		content = {"detail":f"Projet {pk} deleted"}

		project.delete()
		return Response(content, status=status.HTTP_204_NO_CONTENT)


class ContributorProject(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id):
		try:
			contributor = models.Contributor.objects.filter(project_id=project_id)
		except Contributor.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = serializers.ContributorGetSerializer(contributor, many=True)
		return Response(serializer.data)
	
	def post(self, request, project_id):
		try:
			project = models.Project.objects.get(pk=project_id)
		except Project.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if project.author != request.user:
			return Response({"response":"You don't have permission to post that."})
		else:
			serializer = serializers.ContributorAddSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save(project_id=project.id)
				return Response(serializer.data, status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, project_id):

		try:
			project = models.Project.objects.get(pk=project_id)
		except Project.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if project.author != request.user:
			return Response({"response":"You don't have permission to delete contributor."})
		else:
			try:
				contributor = models.Contributor.objects.filter(project_id=project_id).get(
					username=request.data['username'])
				contributor_deleted.delete()
				content = {"response": f"contributor {request.data['username']} deleted"}
				return Response(content)
			except Contributor.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)


class IssueList(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id):
		try:
			project = models.Project.objects.get(id=project_id)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)
		issues = models.Issue.objects.all()
		serializer = serializers.IssueSerializer(issues, many=True)
		return Response(serializer.data)

	def post(self, request, project_id):
		try:
			project = models.Project.objects.get(id=project_id)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = serializers.IssuePostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(project_id=project_id, assignee_user_id=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueDetail(APIView):

	permission_classes = [IsAuthenticated]

	def put(self, request, project_id, issue_id):
		try:
			issue = models.Issue.objects.filter(project_id=project_id).get(pk=issue_id)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = serializers.IssuePostSerializer(issue, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, project_id, issue_id):
		try:
			issue = models.Issue.objects.filter(project_id=project_id).get(pk=issue_id)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		issue.delete()
		content = {"detail":f"issue {issue_id} deleted"}
		return Response(content, status=status.HTTP_204_NO_CONTENT)


class Comment(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id, issue_id):
		try:
			comments = models.Comment.objects.filter(issue_id=issue_id)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = serializers.CommentSerializer(comments, many=True)
		return Response(serializer.data)

	def post(self, request, project_id, issue_id):
		try:
			issue = models.Issue.objects.get(pk=issue_id)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = serializers.CommentPostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(issue_id=issue, author_id=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id, issue_id, comment_id):
		comment = models.Comment.objects.get(pk=comment_id)
		serializer = serializers.CommentSerializer(comment)
		return Response(serializer.data)

	def put(self, request, project_id, issue_id, comment_id):
		issue = models.Issue.objects.get(pk=issue_id)
		comment = models.Comment.objects.get(pk=comment_id)
		serializer = serializers.CommentPostSerializer(comment, data=request.data)
		if serializer.is_valid():
			serializer.save(issue_id=issue, author_id=request.user)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, project_id, issue_id, comment_id):
		comment = models.Comment.objects.get(pk=comment_id)
		comment.delete()
		content = {"detail":f"comment_id {comment_id} deleted"}
		return Response(content)










