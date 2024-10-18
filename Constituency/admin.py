from django.contrib import admin

from .models import ParlimentaryConstituencyModel, AssemblyConstituencyModel, StateModel


class StateAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


class AssemblyConstituencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'parlimentary_constituency_id']
    list_filter = ['parlimentary_constituency_id']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['parlimentary_constituency_id', 'name']


class ParlimentaryConstituencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'state_id']
    list_filter = ['state_id']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['state_id', 'name']


admin.site.register(StateModel, StateAdmin)
admin.site.register(AssemblyConstituencyModel, AssemblyConstituencyAdmin)
admin.site.register(ParlimentaryConstituencyModel, ParlimentaryConstituencyAdmin)
