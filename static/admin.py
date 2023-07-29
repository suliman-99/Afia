from django.contrib import admin
from static.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    readonly_fields = ['name']
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country']
    fields = ['id', 'name', 'country']
    readonly_fields = ['id', 'name', 'country']
    search_fields = ['name', 'country__name']


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'icon']
    fields = ['name', 'description', 'icon']
    readonly_fields = ['name']
    search_fields = ['name', 'description']

