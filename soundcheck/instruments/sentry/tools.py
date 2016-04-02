from django.utils import timezone

import requests

from .. import models
from .. import app_settings


class SentryDataRetriever(object):

    def __init__(self, datetime=timezone.now()):

        resp = requests.get(
            app_settings.SENTRY_API_URL,
            headers=app_settings.SENTRY_API_HEADERS)

        issues = resp.json()

        models.Sentry.objects.create(
            nb_unresolved_issues=len(issues),
            datetime=datetime)

        for appname in app_settings.FOLLOWED_APPS:
            nb_app_issues = 0
            for issue in issues:
                if issue["culprit"].startswith(appname):
                    nb_app_issues += 1
            models.Sentry.objects.create(
                nb_unresolved_issues=nb_app_issues,
                django_app=appname,
                datetime=datetime)
