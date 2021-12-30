from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

""" accounts : 
		admin-oc, password-oc
		admin, Se3cret!
"""

class User(AbstractUser):
	
	def __str__(self):
		return self.first_name


class Contributor(models.Model):

	user_id = models.IntegerField()
	project_id = models.IntegerField()
	permission = models.CharField(max_length=255)
	role = models.CharField(max_length=255)

class Project(models.Model):

	class ProjectType(models.TextChoices):
		backend = 'Back-end'
		frontend = 'Front-end'
		ios = 'iOS'
		android = 'Android'

	title = models.CharField(max_length=255)
	description = models.TextField(max_length=8192, blank=True)
	projet_type = models.CharField(max_length=128, choices=ProjectType.choices)
	author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

class Issue(models.Model):

	class Priority(models.TextChoices):
		weak = 'Weak'
		meduim = 'Meduim'
		high = 'High'

	title = models.CharField(max_length=128)
	description = models.TextField(max_length=8192)
	tag = models.CharField(max_length=128)
	priority = models.CharField(max_length=128, choices=Priority.choices)
	project_id = models.IntegerField()
	status = models.CharField(max_length=128)
	assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.title

class Comment(models.Model):
	description = models.TextField(max_length=8192)
	author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='author')
	issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='issue')
	created_time = models.DateTimeField(auto_now_add=True)