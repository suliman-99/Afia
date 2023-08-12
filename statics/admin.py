from django.contrib import admin
from django.utils.html import format_html
from statics.models import *


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
    list_display = ['id', 'name', 'description', '_clickable_icon']
    fields = ['id', 'name', 'description', '_clickable_icon', 'icon']
    readonly_fields = ['id', '_clickable_icon']
    search_fields = ['id', 'name', 'description']

    def _clickable_icon(self, specialization:Specialization):
        html = '<a href="{link}"><img src="{photo}" width=100 height=100 /></a>'
        if specialization.icon:
            return format_html(html, link=specialization.icon.url, photo=specialization.icon.url)
        return format_html('<strong> _ <strong>')

