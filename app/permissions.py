from rest_framework import permissions
from django.db import models


class IsContrubutorOrIsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.author.id

