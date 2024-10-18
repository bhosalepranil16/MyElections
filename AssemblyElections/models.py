from django.db import models

from Constituency.models import StateModel, AssemblyConstituencyModel
from Candidate.models import CandidateModel
from PoliticalParty.models import PoliticalPartyModel, AllianceModel


class AssemblyElectionModel(models.Model):
    state_id = models.ForeignKey(StateModel, models.SET_NULL, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=10, null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Assembly Election'
        verbose_name_plural = 'Assembly Elections'


class AssemblyElectionToAssemblyConstituencyModel(models.Model):
    constituency_types = [
        ('GEN', 'General'),
        ('SC', 'Schedule Cast'),
        ('ST', 'Schedule Tribe')
    ]
    assembly_election_id = models.ForeignKey(AssemblyElectionModel, models.SET_NULL, null=True, blank=True)
    assembly_constituency_id = models.ForeignKey(AssemblyConstituencyModel, models.SET_NULL, null=True,
                                                 blank=True)
    type = models.CharField(max_length=10, choices=constituency_types, null=True, blank=True)
    electors = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    date_of_poll = models.DateField(null=True, blank=True)
    date_of_result = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Year: {self.assembly_election_id}, Constituency: {self.assembly_constituency_id}'

    class Meta:
        verbose_name = 'Assembly Election To Assembly Constituency'
        verbose_name_plural = 'Assembly Election To Assembly Constituencies'
        unique_together = ['assembly_election_id', 'assembly_constituency_id']


class AssemblyElectionToAssemblyConstituencyToCandidateModel(models.Model):
    assembly_election_to_assembly_constituency_id = models.ForeignKey(
        AssemblyElectionToAssemblyConstituencyModel, models.SET_NULL, null=True, blank=True)
    candidate_id = models.ForeignKey(CandidateModel, models.SET_NULL, null=True, blank=True)
    political_party_id = models.ForeignKey(PoliticalPartyModel, models.SET_NULL, null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.assembly_election_to_assembly_constituency_id}, Candidate: {self.candidate_id}, Political Party: {self.political_party_id}'

    class Meta:
        verbose_name = 'Assembly Election To Assembly Constituency To Candidate'
        verbose_name_plural = 'Assembly Election To Assembly Constituency To Candidates'
        unique_together = ['assembly_election_to_assembly_constituency_id', 'candidate_id',
                           'political_party_id']


class AssemblyElectionToAllianceModel(models.Model):
    assembly_election_id = models.ForeignKey(AssemblyElectionModel, models.SET_NULL, null=True, blank=True)
    alliance_id = models.ForeignKey(AllianceModel, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Year: {self.assembly_election_id},  Alliance: {self.alliance_id}'

    class Meta:
        verbose_name = 'Assembly Election To Alliance'
        verbose_name_plural = 'Assembly Election To Alliance'
        unique_together = ['assembly_election_id', 'alliance_id']


class AssemblyElectionToAllianceToPoliticalPartyModel(models.Model):
    assembly_election_to_alliance_id = models.ForeignKey(AssemblyElectionToAllianceModel, models.SET_NULL,
                                                             null=True, blank=True)
    political_party_id = models.ForeignKey(PoliticalPartyModel, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.assembly_election_to_alliance_id},  Political Party: {self.political_party_id}'

    class Meta:
        verbose_name = 'Assembly Election To Alliance To Political Party'
        verbose_name_plural = 'Assembly Election To Alliance To Political Parties'
        unique_together = ['assembly_election_to_alliance_id', 'political_party_id']
