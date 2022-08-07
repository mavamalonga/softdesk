from django.contrib import admin
from APIREST import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    filter_horizontal = ('contributors',)


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assignee_user')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'issue', 'description')


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.User, UserAdmin)
