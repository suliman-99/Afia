from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin
from django.utils.html import format_html
from Auth.models import *


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'email_verified', 'phone_number', '_clickable_photo', 'birth_date', 'gender', 'city', 'first_name', 'last_name', 'role', 'accepted', 'is_active', 'is_staff', 'is_superuser']

    fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': (
                "password",
                "id", "email", "email_verified", "role", 'accepted', "is_active", "is_staff", "is_superuser",
                "first_name", "last_name", 
                "phone_number", "birth_date", "gender", "_clickable_photo", "photo", "city", 
                "blood_type", "length", "weight", "chronic_disease", "genetic_disease", "other_info", 
                "license", "available_for_meeting", "specialization",
                "groups", 
            )
        }
    ),)
    
    readonly_fields = ['id', '_clickable_photo']

    def _clickable_photo(self, user:User):
        html = '<a href="{link}"><img src="{photo}" width=100 height=100 /></a>'
        if user.photo:
            return format_html(html, link=user.photo.url, photo=user.photo.url)
        return format_html('<strong> _ <strong>')


admin.site.unregister(BaseGroup)
admin.site.register(Group, BaseGroupAdmin)

