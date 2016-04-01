from django.db import models

from .. import mixins


class Git(mixins.SoundcheckBaseModel):
    """Store git data."""
    nb_commits = models.PositiveIntegerField()
    nb_files = models.PositiveIntegerField()
    nb_lines = models.PositiveIntegerField()
