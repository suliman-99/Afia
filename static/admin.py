from django.contrib import admin
from static.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    readonly_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country']
    fields = ['id', 'name', 'country']
    readonly_fields = ['id', 'name', 'country']


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    readonly_fields = ['name']

