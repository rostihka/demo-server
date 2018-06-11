from rest_framework import permissions


class SafeMethodsOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class PostAuthorCanEditPermission(SafeMethodsOnlyPermission):
    def has_object_permission(self, request, view, obj=None):
        if obj is None:
            can_edit = True
        else:
            can_edit = request.user == obj.autor
        return can_edit or super(PostAuthorCanEditPermission, self).has_object_permission(request, view, obj)