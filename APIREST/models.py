from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
	
	def __str__(self):
		return self.first_name


class Project(models.Model):
	TAG_CHOICES = (
        ('w', 'application web'),
        ('l', 'logiciel desktop'),
		('m', 'application mobile'),
		('o', 'other'),
    )

	title = models.CharField(max_length=255)
	description = models.TextField(max_length=8192, blank=True)
	tag = models.CharField(max_length=1, choices=TAG_CHOICES)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	Contributors = models.ManyToManyField(User, related_name='contributors')
	
	def __str__(self):
		return self.title
	

class Issue(models.Model):
	STATUS_CHOICES = (
        ('o', 'Open'),
        ('r', 'resolved'),
    )

	title = models.CharField(max_length=128)
	description = models.TextField(max_length=8192)
	project = models.ForeignKey(Project, related_name='project', on_delete=models.CASCADE)
	status =  models.CharField(max_length=1, choices=STATUS_CHOICES)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True) 
	assignee_user = models.ForeignKey(User, related_name='assignee_user', on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Comment(models.Model):
	description = models.TextField(max_length=8192)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='author')
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='issue')
	created_time = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.author
