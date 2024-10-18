from django.contrib import admin

from .models import AssemblyElectionModel, AssemblyElectionToAssemblyConstituencyModel, \
    AssemblyElectionToAssemblyConstituencyToCandidateModel, AssemblyElectionToAllianceModel, AssemblyElectionToAllianceToPoliticalPartyModel


class AssemblyElectionAdmin(admin.ModelAdmin):
    list_display = ['state_id', 'year']
    prepopulated_fields = {'slug': ('year',)}
    ordering = ['year']


class AssemblyElectionToAssemblyConstituencyAdmin(admin.ModelAdmin):
    list_display = ['assembly_election_id', 'assembly_constituency_id', 'type', 'electors', 'date_of_poll',
                    'date_of_result']
    list_filter = ['assembly_election_id', 'assembly_constituency_id', 'type', 'date_of_poll']
    ordering = ['-id']


class AssemblyElectionToAssemblyConstituencyToCandidateAdmin(admin.ModelAdmin):
    list_display = ['assembly_election_to_assembly_constituency_id', 'candidate_id', 'political_party_id',
                    'votes']
    list_filter = ['assembly_election_to_assembly_constituency_id', 'candidate_id', 'political_party_id']


class AssemblyElectionToAllianceAdmin(admin.ModelAdmin):
    list_display = ['assembly_election_id', 'alliance_id']
    list_filter = ['assembly_election_id', 'alliance_id']


class AssemblyElectionToAllianceToPoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ['assembly_election_to_alliance_id', 'political_party_id']
    list_filter = ['assembly_election_to_alliance_id', 'political_party_id']


admin.site.register(AssemblyElectionModel, AssemblyElectionAdmin)
admin.site.register(AssemblyElectionToAssemblyConstituencyModel, AssemblyElectionToAssemblyConstituencyAdmin)
admin.site.register(AssemblyElectionToAssemblyConstituencyToCandidateModel,
                    AssemblyElectionToAssemblyConstituencyToCandidateAdmin)
admin.site.register(AssemblyElectionToAllianceModel, AssemblyElectionToAllianceAdmin)
admin.site.register(AssemblyElectionToAllianceToPoliticalPartyModel, AssemblyElectionToAllianceToPoliticalPartyAdmin)
