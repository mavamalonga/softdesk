from rest_framework import permissions
from django.db import models


class IsContrubutorAndOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ["GET", "POST"]:
            try:
                """only contrubutor post"""
                return request.user.id == obj.author.id
            except:
                pass
            return request.user.id == obj.user
        else:
            return request.user.id == obj.author.id

