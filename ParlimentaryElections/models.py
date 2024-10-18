from django.db import models

from PoliticalParty.models import PoliticalPartyModel, AllianceModel
from Constituency.models import ParlimentaryConstituencyModel
from Candidate.models import CandidateModel


class ParlimentaryElectionModel(models.Model):
    year = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=10, null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Parlimentary Election'
        verbose_name_plural = 'Parlimentary Elections'


class ParlimentaryElectionToParlimentaryConstituencyModel(models.Model):
    constituency_types = [
        ('GEN', 'General'),
        ('SC', 'Schedule Cast'),
        ('ST', 'Schedule Tribe')
    ]

    parlimentary_election_id = models.ForeignKey(ParlimentaryElectionModel, models.SET_NULL, null=True, blank=True)
    parlimentary_constituency_id = models.ForeignKey(ParlimentaryConstituencyModel, models.SET_NULL, null=True,
                                                     blank=True)
    type = models.CharField(max_length=10, choices=constituency_types, null=True, blank=True)
    electors = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    date_of_poll = models.DateField(null=True, blank=True)
    date_of_result = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Year: {self.parlimentary_election_id}, Constituency: {self.parlimentary_constituency_id}'

    class Meta:
        verbose_name = 'Parlimentary Election To Parlimentary Constituency'
        verbose_name_plural = 'Parlimentary Election To Parlimentary Constituencies'
        unique_together = ['parlimentary_election_id', 'parlimentary_constituency_id']


class ParlimentaryElectionToParlimentaryConstituencyToCandidateModel(models.Model):
    parlimentary_election_to_parlimentary_constituency_id = models.ForeignKey(
        ParlimentaryElectionToParlimentaryConstituencyModel, models.SET_NULL, null=True, blank=True)
    candidate_id = models.ForeignKey(CandidateModel, models.SET_NULL, null=True, blank=True)
    political_party_id = models.ForeignKey(PoliticalPartyModel, models.SET_NULL, null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.parlimentary_election_to_parlimentary_constituency_id}, Candidate: {self.candidate_id}, Political Party: {self.political_party_id}'

    class Meta:
        verbose_name = 'Parlimentary Election To Parlimentary Constituency To Candidate'
        verbose_name_plural = 'ParlimentaryElection To Parlimentary Constituency To Candidates'
        unique_together = ['parlimentary_election_to_parlimentary_constituency_id', 'candidate_id',
                           'political_party_id']


class ParlimentaryElectionToAllianceModel(models.Model):
    parlimentary_election_id = models.ForeignKey(ParlimentaryElectionModel, models.SET_NULL, null=True, blank=True)
    alliance_id = models.ForeignKey(AllianceModel, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Year: {self.parlimentary_election_id},  Alliance: {self.alliance_id}'

    class Meta:
        verbose_name = 'Parlimentary Election To Alliance'
        verbose_name_plural = 'Parlimentary Election To Alliance'
        unique_together = ['parlimentary_election_id', 'alliance_id']


class ParlimentaryElectionToAllianceToPoliticalPartyModel(models.Model):
    parlimentary_election_to_alliance_id = models.ForeignKey(ParlimentaryElectionToAllianceModel, models.SET_NULL,
                                                             null=True, blank=True)
    political_party_id = models.ForeignKey(PoliticalPartyModel, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.parlimentary_election_to_alliance_id},  Political Party: {self.political_party_id}'

    class Meta:
        verbose_name = 'Parlimentary Election To Alliance To Political Party'
        verbose_name_plural = 'Parlimentary Election To Alliance To Political Parties'
        unique_together = ['parlimentary_election_to_alliance_id', 'political_party_id']
