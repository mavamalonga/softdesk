from rest_framework import permissions

class IsContrubutorOrIsOwner(permissions.BasePermission):
    message = 'Permission only to the contributors members.'

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return True
        return request.user in obj.contributors
