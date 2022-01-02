from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from app import models 
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(ModelSerializer):

	class Meta:
		models.User
		fields = ['username', 'email', 'first_name', 'last_name']


class SignUpSerializer(ModelSerializer):
    email = serializers.EmailField(
    	required=True,
    	validators=[UniqueValidator(queryset=models.User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = models.User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user


class ProjectViewGetSerializer(ModelSerializer):

	class Meta:
		model = models.Project
		fields = ['id', 'title', 'description', 'projet_type']

class ProjectViewPostSerializer(ModelSerializer):

	class Meta:
		model = models.Project
		fields = ['title', 'description', 'projet_type']


class ProjectDetailSerializer(ModelSerializer):

	issues = SerializerMethodField()

	class Meta:
		model = models.Project
		fields = ['id', 'title', 'description', 'projet_type', 'issues']

	def get_issues(self, instance):
		queryset = models.Issue.objects.filter(project_id=instance.id)
		serializer = IssueSerializer(queryset, many=True)
		return serializer.data


class ContributorSerializer(ModelSerializer):

	class Meta:
		model = models.Contributor
		fields = ['user', 'project_id', 'permission', 'role']


class ContributorAddSerializer(ModelSerializer):

	class Meta:
		model = models.Contributor
		fields = ('user', 'permission', 'role')
		extra_kwargs = {
			'user': {'required': True},
			'permission':{'required':True},
			'role':{'required':True}
		}

class ContributorGetSerializer(ModelSerializer):

	class Meta:
		model = models.Contributor
		fields = ['user', 'project_id', 'permission', 'role']



class IssueSerializer(ModelSerializer):

	comments = SerializerMethodField()

	class Meta:
		model = models.Issue
		fields = ['id', 'title', 'project_id', 'description', 'tag', 'priority', 'status', 
			'author', 'created_time', 'comments']

	def get_comments(self, instance):
		queryset = models.Comment.objects.filter(issue_id=instance.id)
		serializer = CommentSerializer(queryset, many=True)
		return serializer.data

class IssuePostSerializer(ModelSerializer):

	class Meta:
		model = models.Issue
		fields = ['title', 'description', 'tag', 'priority', 'status']


class CommentSerializer(ModelSerializer):

	class Meta:
		model = models.Comment
		fields = ['id', 'author', 'description', 'created_time']

class CommentPostSerializer(ModelSerializer):

	class Meta:
		model = models.Comment
		fields = ['description']
