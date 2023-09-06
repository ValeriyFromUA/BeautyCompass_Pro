from rest_framework.permissions import IsAdminUser, BasePermission


class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET'] or IsAdminUser().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return request.method not in ['PUT', 'PATCH', 'DELETE'] or IsAdminUser().has_permission(request, view)


class CompanyDetailsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'POST'] or IsAdminUser().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return request.method not in ['PUT', 'PATCH', 'DELETE'] or IsAdminUser().has_permission(request, view)
