from rest_framework.permissions import BasePermission


class IsProjectManager(BasePermission):

    def has_permission(self, request, view):
        if request.user.userprofile.role == 2 and request.user:
            return True


