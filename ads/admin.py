from django.contrib import admin
from .models import Ad, Category, Location, User
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AdResource(resources.ModelResource):
    class Meta:
        model = Ad


class AdAdmin(ImportExportModelAdmin):
    resource_class = AdResource


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource


class LocationResource(resources.ModelResource):
    class Meta:
        model = Location


class LocationAdmin(ImportExportModelAdmin):
    resource_class = LocationResource


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


admin.site.register(Ad, AdAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(User, UserAdmin)
