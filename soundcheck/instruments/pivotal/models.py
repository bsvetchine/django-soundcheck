from django.db import models

from .. import mixins


class Pivotal(mixins.SoundcheckBaseModel):
    """Store git data."""
    nb_stories = models.PositiveIntegerField()
    nb_features = models.PositiveIntegerField()
    nb_bugs = models.PositiveIntegerField()
    nb_chores = models.PositiveIntegerField()
    nb_releases = models.PositiveIntegerField()
    average_feature_point = models.DecimalField()
    nb_delivered_stories = models.PositiveIntegerField()
    nb_finished_stories = models.PositiveIntegerField()
    nb_rejected_stories = models.PositiveIntegerField()
    nb_started_stories = models.PositiveIntegerField()
    nb_unstarted_stories = models.PositiveIntegerField()
