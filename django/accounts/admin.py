from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, School, UserGroup


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'get_full_name',
        'email',
        'nationality',
        'school',
        'gender',
    )
    list_filter = (
        'gender',
        'nationality',
        'school',
    )


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
    )
    list_filter = (
        'country',
    )


admin.site.unregister(Group)
admin.site.register(UserGroup)
