from django.db import models

from ... import mixins


class Sentry(mixins.SoundcheckBaseModel):
    """Store git data."""
    nb_unresolved_issues = models.PositiveIntegerField()
