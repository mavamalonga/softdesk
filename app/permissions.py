from rest_framework import permissions
from django.db import models


class ApiPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return request.user.id == obj.id
        else:
            return request.user.id == obj.author.id

