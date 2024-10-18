from django.contrib import admin

from .models import CandidateModel


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


admin.site.register(CandidateModel, CandidateAdmin)
