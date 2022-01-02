from rest_framework import permissions
from app import models

class ContributorOnly(permissions.BasePermission):

    edit_methods = ("GET",)

    def has_object_permission(self, request, view, obj):
        if request.is_authenticated and request.method in self.edit_methods:
            return request.user.id == obj.id


class CreatorOnly(permissions.BasePermission):

    edit_methods = ("GET","PUT", "PATCH", "DELETE")

    def has_object_permission(self, request, view, obj):
        if request.is_authenticated and request.method in self.edit_methods:
            return request.user.id == obj.author


"""
contributor = models.Contributor.objects.filter(
            project_id=project_id).get(username=request.user.author)
        self.check_object_permissions(self.request, contributor)



class Contributor(permissions.BasePermission):

    edit_methods = ("GET")

    def has_object_permission(self, request, view, obj):
        if request.method in self.edit_methods:
            contributor = models.Contributor.objects.filter(project_id=project_id).get(username=request.user.username)
            return True
        return obj.username == request.user
"""
""""
project = models.Project.objects.filter(project_id=project_id)
if project.author == request.user:
    return True

contributor = models.Contributor.objects.filter(project_id=project_id).get(username=request.user.username)
if user.username == request.user:
    return True

issue = models.Issue.objects.filter(project_id=project_id).get(pk=issue_id)
if issue.assignee_user != request.user:
    return True

"""
