from rest_framework import permissions
from . permissions import IsStaffEditorPermission, MyPermission

class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser ,
        IsStaffEditorPermission ,
        MyPermission
        ]
    

class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False
    def get_queryset(self):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset()
        if self.allow_staff_view and self.request.user.is_staff:
            return qs
        return qs.filter(**lookup_data)