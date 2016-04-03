from django.db import models

from .. import mixins


class Prospector(mixins.SoundcheckBaseModel):
    """Store prospector data."""
    nb_messages = models.PositiveIntegerField()
