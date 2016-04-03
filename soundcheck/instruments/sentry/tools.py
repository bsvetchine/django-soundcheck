from django.utils import timezone

import requests

from . import settings
from ... import models
from ... import app_settings


class SentryDataRetriever(object):

    def __init__(self, datetime=timezone.now()):

        resp = requests.get(
            settings.SENTRY_API_URL,
            headers=settings.SENTRY_API_HEADERS)

        issues = resp.json()

        models.Sentry.objects.create(
            nb_unresolved_issues=len(issues),
            datetime=datetime)

        for app_name in app_settings.FOLLOWED_APPS:
            nb_app_issues = 0
            for issue in issues:
                if issue["culprit"].startswith(app_name):
                    nb_app_issues += 1
            models.Sentry.objects.create(
                nb_unresolved_issues=nb_app_issues,
                app_name=app_name,
                datetime=datetime)
