from rest_framework import permissions

"""
Admin users can get a list of all users
Only admin users can delete users
Everyone can create a user/register
Logged in users can only update their own profile
"""

class IsLoggedInUserOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsAdminUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    
    
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff