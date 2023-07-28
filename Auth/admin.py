from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin
from Auth.models import *


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'email_verified', 'role', 'is_active', 'is_staff', 'is_superuser']

    fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': (
                "id", "email", "email_verified", "role", "is_active", "is_staff", "is_superuser",
                "first_name", "last_name", 
                "phone_number", "birth_date", "gender", "photo", "city", 
                "blood_type", "length", "weight", "chronic_disease", "genetic_disease", "other_info", 
                "license", "available_for_meeting", "specialization",
                "groups", 
            )
        }
    ),)
    readonly_fields = ['id']


admin.site.unregister(BaseGroup)
admin.site.register(Group, BaseGroupAdmin)

