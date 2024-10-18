from django.db import models


class PoliticalPartyModel(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    short_name = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(max_length=128, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Political Party'
        verbose_name_plural = 'Political Parties'


class AllianceModel(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=128, null=True, blank=True, unique=True)
    short_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Alliance'
        verbose_name_plural = 'Alliance'
