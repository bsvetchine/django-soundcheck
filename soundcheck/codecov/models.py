from django.db import models

from .. import mixins


class Codecov(mixins.SoundcheckBaseModel):
    """Store codecov data."""
    coverage = models.PositiveIntegerField()
    hit = models.PositiveIntegerField()
    partial = models.PositiveIntegerField()
    branches = models.PositiveIntegerField()
    lines = models.PositiveIntegerField()
    missed = models.PositiveIntegerField()
    files = models.PositiveIntegerField()
