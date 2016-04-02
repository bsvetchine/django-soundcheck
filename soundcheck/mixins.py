from django.db import models


class SoundcheckBaseModel(models.Model):
    """."""
    app_name = models.TextField()
    datetime = models.DateTimeField()

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)
        abstract = True
