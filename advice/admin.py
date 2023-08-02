from django.contrib import admin
from advice.models import Advice


@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    fields = ['id', 'content']
    readonly_fields = ['id']
    search_fields = ['id', 'content']

