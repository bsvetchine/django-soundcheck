import base64

from django.conf import settings

import requests


SENTRY_API_TOKEN = getattr(settings, "SENTRY_API_TOKEN")
SENTRY_ORGANIZATION_SLUG = getattr(settings, "SENTRY_ORGANIZATION_SLUG")
SENTRY_PROJECT_SLUG = getattr(settings, "SENTRY_PROJECT_SLUG")

ENABLE_SENTRY = True if SENTRY_API_TOKEN else False

if ENABLE_SENTRY:
    SENTRY_API_BASE64_TOKEN = base64.b64encode(
        "{user_token}:".format(user_token=SENTRY_API_TOKEN))
    SENTRY_API_HEADERS = {
        "Host": "app.getsentry.com",
        "Authorization": "Basic {b64_token}".format(
            b64_token=SENTRY_API_BASE64_TOKEN)
    }
    SENTRY_API_URL = (
        "https://app.getsentry.com/api/0/projects/{org}/{proj}/issues/".format(
            org=SENTRY_ORGANIZATION_SLUG, proj=SENTRY_PROJECT_SLUG)
    )
    resp = requests.get(SENTRY_API_URL, headers=SENTRY_API_HEADERS)
    if not resp.status_code != 200:
        raise Exception(
            "Unable to retrieve Sentry data (status_code={status_code}). "
            "Please check the following settings : "
            "SENTRY_API_TOKEN, SENTRY_ORGANIZATION_SLUG, SENTRY_PROJECT_SLUG"
            .format(status_code=resp.status_code))
