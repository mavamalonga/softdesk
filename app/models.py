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

	username = models.IntegerField()
	project_id = models.IntegerField()
	permission = models.CharField(max_length=255)
	role = models.CharField(max_length=255)

class Project(models.Model):

	title = models.CharField(max_length=255)
	description = models.TextField(max_length=8192, blank=True)
	projet_type = models.CharField(max_length=128)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

class Issue(models.Model):

	title = models.CharField(max_length=128)
	description = models.TextField(max_length=8192)
	tag = models.CharField(max_length=128)
	priority = models.CharField(max_length=128)
	project_id = models.IntegerField()
	status = models.CharField(max_length=128)
	assignee_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.title

class Comment(models.Model):
	description = models.TextField(max_length=8192)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='author')
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='issue')
	created_time = models.DateTimeField(auto_now_add=True)