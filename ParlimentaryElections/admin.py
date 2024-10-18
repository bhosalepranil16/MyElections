from django.contrib import admin

from .models import ParlimentaryElectionModel, ParlimentaryElectionToParlimentaryConstituencyModel, \
    ParlimentaryElectionToParlimentaryConstituencyToCandidateModel, ParlimentaryElectionToAllianceModel, \
    ParlimentaryElectionToAllianceToPoliticalPartyModel


class ParlimentaryElectionAdmin(admin.ModelAdmin):
    list_display = ['year']
    prepopulated_fields = {'slug': ('year',)}
    ordering = ['year']


class ParlimentaryElectionToParlimentaryConstituencyAdmin(admin.ModelAdmin):
    list_display = ['parlimentary_election_id', 'parlimentary_constituency_id', 'type', 'electors', 'date_of_poll',
                    'date_of_result']
    list_filter = ['parlimentary_election_id', 'parlimentary_constituency_id', 'type', 'date_of_poll']
    ordering = ['-id']


class ParlimentaryElectionToParlimentaryConstituencyToCandidateAdmin(admin.ModelAdmin):
    list_display = ['parlimentary_election_to_parlimentary_constituency_id', 'candidate_id', 'political_party_id',
                    'votes']
    list_filter = ['parlimentary_election_to_parlimentary_constituency_id', 'candidate_id', 'political_party_id']


class ParlimentaryElectionToAllianceAdmin(admin.ModelAdmin):
    list_display = ['parlimentary_election_id', 'alliance_id']
    list_filter = ['parlimentary_election_id', 'alliance_id']


class ParlimentaryElectionToAllianceToPoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ['parlimentary_election_to_alliance_id', 'political_party_id']
    list_filter = ['parlimentary_election_to_alliance_id', 'political_party_id']


admin.site.register(ParlimentaryElectionModel, ParlimentaryElectionAdmin)
admin.site.register(ParlimentaryElectionToParlimentaryConstituencyModel,
                    ParlimentaryElectionToParlimentaryConstituencyAdmin)
admin.site.register(ParlimentaryElectionToParlimentaryConstituencyToCandidateModel,
                    ParlimentaryElectionToParlimentaryConstituencyToCandidateAdmin)
admin.site.register(ParlimentaryElectionToAllianceModel, ParlimentaryElectionToAllianceAdmin)
admin.site.register(ParlimentaryElectionToAllianceToPoliticalPartyModel,
                    ParlimentaryElectionToAllianceToPoliticalPartyAdmin)
