from rest_framework import permissions
from . permissions import IsStaffEditorPermission, MyPermission

class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser ,
        IsStaffEditorPermission ,
        MyPermission
        ]