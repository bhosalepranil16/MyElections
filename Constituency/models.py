from django.db import models


class StateModel(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=128, null=True, blank=True, unique=True)
    state_from = models.IntegerField(null=True, blank=True)
    state_to = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'


class ParlimentaryConstituencyModel(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=128, null=True, blank=True, unique=True)
    state_id = models.ForeignKey(StateModel, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Parlimentary Constituency'
        verbose_name_plural = 'Parlimentary Constituencies'


class AssemblyConstituencyModel(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=128, null=True, blank=True, unique=True)
    parlimentary_constituency_id = models.ForeignKey(ParlimentaryConstituencyModel, models.SET_NULL, null=True,
                                                     blank=True)
    state_id = models.ForeignKey(StateModel, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Assembly Constituency'
        verbose_name_plural = 'Assembly Constituencies'
