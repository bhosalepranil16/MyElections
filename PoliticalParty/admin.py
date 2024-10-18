from django.contrib import admin

from .models import PoliticalPartyModel, AllianceModel


class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


class AllianceAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


admin.site.register(AllianceModel, AllianceAdmin)
admin.site.register(PoliticalPartyModel, PoliticalPartyAdmin)
