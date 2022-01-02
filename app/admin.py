from django.contrib import admin
from app import models

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')

class IssueAdmin(admin.ModelAdmin):
	list_display = ('title', )

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', )

class ContributorAdmin(admin.ModelAdmin):
	list_display = ('user', )

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', )
		
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Contributor, ContributorAdmin)
admin.site.register(models.User, UserAdmin)