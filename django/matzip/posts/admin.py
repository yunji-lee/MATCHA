from django.contrib import admin
from .models import Post, Matzip_list, Star
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.conf import settings

# User = settings.AUTH_USER_MODEL


class PostResource(resources.ModelResource):

    class Meta:
        model = Post


class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource


class Matzip_listResource(resources.ModelResource):

    class Meta:
        model = Matzip_list


class Matzip_listAdmin(ImportExportModelAdmin):
    resource_class = Matzip_listResource


# class UserResource(resources.ModelResource):
#
#     class Meta:
#         model = User
#
#
# class UseAdmin(ImportExportModelAdmin):
#     resource_class = UserResource
# Register your models here.


admin.site.register(Post, PostAdmin)
# admin.site.register(User, UseAdmin)
admin.site.register(Matzip_list, Matzip_listAdmin)
admin.site.register(Star)