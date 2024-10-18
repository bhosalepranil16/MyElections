from django.db import models


class CandidateModel(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=128, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'
