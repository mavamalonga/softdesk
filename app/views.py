from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app import models, serializers

@api_view(['GET', 'POST'])
def project_list(request):

	if request.method == 'GET':
		projects = models.Project.objects.all()
		serializer = serializers.ProjectSerializer(projects, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = serializers.ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.author_user_id = request.user.id
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
	"""
	Retrive, update or delete a code project
	"""
	try:
		project = models.Project.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = serializers.ProjectSerializer(project)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = serializers.ProjectSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		project.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



