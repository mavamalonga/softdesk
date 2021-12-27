from django.contrib import admin
from app import models

class ProjectsAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')

"""
class UserAdmin(admin.ModelAdmin):
	list_display = ('fist_name', )

class ContributorsAdmin(admin.ModelAdmin):
	list_display = ('user_id', )

class IssuesAdmin(admin.ModelAdmin):
	list_display = ('title', )

class CommentsAdmin(admin.ModelAdmin):
	list_display = ('author_id', )
		
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Contributors, ContributorsAdmin)
admin.site.register(models.Issues, IssuesAdmin)
admin.site.register(models.Comments, CommentsAdmin)
"""
admin.site.register(models.Projects, ProjectsAdmin)