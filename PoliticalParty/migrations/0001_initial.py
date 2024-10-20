# Generated by Django 4.1.5 on 2024-10-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllianceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('slug', models.SlugField(blank=True, max_length=128, null=True, unique=True)),
                ('short_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Alliance',
                'verbose_name_plural': 'Alliance',
            },
        ),
        migrations.CreateModel(
            name='PoliticalPartyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('short_name', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.SlugField(blank=True, max_length=128, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Political Party',
                'verbose_name_plural': 'Political Parties',
            },
        ),
    ]
