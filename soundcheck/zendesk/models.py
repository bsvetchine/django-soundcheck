from django.db import models

from .. import mixins


class Sendesk(mixins.SoundcheckBaseModel):
    """Store git data."""
    nb_tickets = models.PositiveIntegerField()
    nb_urgent_tickets = models.PositiveIntegerField()
    nb_high_tickets = models.PositiveIntegerField()
    nb_normal_tickets = models.PositiveIntegerField()
    nb_low_tickets = models.PositiveIntegerField()
    nb_new_tickets = models.PositiveIntegerField()
    nb_open_tickets = models.PositiveIntegerField()
    nb_pending_tickets = models.PositiveIntegerField()
    nb_hold_tickets = models.PositiveIntegerField()
