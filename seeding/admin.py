from django.contrib import admin
from seeding.models import AppliedSeeder

@admin.register(AppliedSeeder)
class AppliedSeederAdmin(admin.ModelAdmin):
    pass


