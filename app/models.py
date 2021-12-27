from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
	
	def __str__(self):
		return self.first_name


class Contributors(models.Model):

	class Permission(models.TextChoices):
		read = 'read'
		update = 'update'
		delete = 'delete'

	user_id = models.IntegerField()
	projet_id = models.IntegerField()
	permission = models.CharField(max_length=25, choices=Permission.choices)
	role = models.CharField(max_length=255)

class Projects(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(max_length=8192, blank=True)
	projet_type = models.CharField(max_length=128) #(back-end, front-end, iOS ou Android)
	author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

class Issues(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField(max_length=8192)
	tag = models.CharField(max_length=128)
	priority = models.CharField(max_length=128) #(FAIBLE, MOYENNE ou ÉLEVÉE),
	project_id = models.IntegerField()
	status = models.CharField(max_length=128)
	assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # l'auteur
	created_time = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.title

class Comments(models.Model):
	description = models.TextField(max_length=8192)
	author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='author')
	issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE, related_name='issue')
	created_time = models.DateTimeField(auto_now_add=True)