# Generated by Django 4.1.5 on 2024-10-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Candidate', '0001_initial'),
        ('PoliticalParty', '0001_initial'),
        ('Constituency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParlimentaryElectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=10, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Parlimentary Election',
                'verbose_name_plural': 'Parlimentary Elections',
            },
        ),
        migrations.CreateModel(
            name='ParlimentaryElectionToAllianceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alliance_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PoliticalParty.alliancemodel')),
                ('parlimentary_election_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ParlimentaryElections.parlimentaryelectionmodel')),
            ],
            options={
                'verbose_name': 'Parlimentary Election To Alliance',
                'verbose_name_plural': 'Parlimentary Election To Alliance',
                'unique_together': {('parlimentary_election_id', 'alliance_id')},
            },
        ),
        migrations.CreateModel(
            name='ParlimentaryElectionToParlimentaryConstituencyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('GEN', 'General'), ('SC', 'Schedule Cast'), ('ST', 'Schedule Tribe')], max_length=10, null=True)),
                ('electors', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('date_of_poll', models.DateField(blank=True, null=True)),
                ('date_of_result', models.DateField(blank=True, null=True)),
                ('parlimentary_constituency_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Constituency.parlimentaryconstituencymodel')),
                ('parlimentary_election_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ParlimentaryElections.parlimentaryelectionmodel')),
            ],
            options={
                'verbose_name': 'Parlimentary Election To Parlimentary Constituency',
                'verbose_name_plural': 'Parlimentary Election To Parlimentary Constituencies',
                'unique_together': {('parlimentary_election_id', 'parlimentary_constituency_id')},
            },
        ),
        migrations.CreateModel(
            name='ParlimentaryElectionToParlimentaryConstituencyToCandidateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(blank=True, null=True)),
                ('candidate_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Candidate.candidatemodel')),
                ('parlimentary_election_to_parlimentary_constituency_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ParlimentaryElections.parlimentaryelectiontoparlimentaryconstituencymodel')),
                ('political_party_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PoliticalParty.politicalpartymodel')),
            ],
            options={
                'verbose_name': 'Parlimentary Election To Parlimentary Constituency To Candidate',
                'verbose_name_plural': 'ParlimentaryElection To Parlimentary Constituency To Candidates',
                'unique_together': {('parlimentary_election_to_parlimentary_constituency_id', 'candidate_id', 'political_party_id')},
            },
        ),
        migrations.CreateModel(
            name='ParlimentaryElectionToAllianceToPoliticalPartyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parlimentary_election_to_alliance_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ParlimentaryElections.parlimentaryelectiontoalliancemodel')),
                ('political_party_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PoliticalParty.politicalpartymodel')),
            ],
            options={
                'verbose_name': 'Parlimentary Election To Alliance To Political Party',
                'verbose_name_plural': 'Parlimentary Election To Alliance To Political Parties',
                'unique_together': {('parlimentary_election_to_alliance_id', 'political_party_id')},
            },
        ),
    ]
