from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_staff
            or (obj.user_id == request.user and obj.actual_return_date is None)
        )
