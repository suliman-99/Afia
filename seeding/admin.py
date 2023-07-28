from django.contrib import admin
from seeding.models import AppliedSeeder

@admin.register(AppliedSeeder)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


