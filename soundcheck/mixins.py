from django.db import models


class SoundcheckBaseModel(models.Model):
    """."""
    django_app = models.TextField()
    date = models.DateTimeField()

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)
        abstract = True
