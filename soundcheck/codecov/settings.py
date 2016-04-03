import requests

from django.conf import settings


# User configurable settings

CODECOV_SERVICE = getattr(settings, "CODEDOV_SERVICE", None)
CODEDOV_USERNAME = getattr(settings, "CODEDOV_USERNAME", None)
CODECOV_API_TOKEN = getattr(settings, "CODECOV_API_TOKEN", None)
CODECOV_REPO_NAME = getattr(settings, "CODEDOV_REPO_NAME", None)


# Internal settings and connection check

ENABLE_CODECOV = True if CODECOV_SERVICE and CODEDOV_USERNAME else False

if ENABLE_CODECOV:
    CODECOV_BASE_URL = (
        "https://codecov.io/api/{service}/{username}/{repo}".format(
            service=CODECOV_SERVICE, username=CODEDOV_USERNAME,
            repo=CODECOV_REPO_NAME)
    )
    if CODECOV_API_TOKEN:
        CODECOV_BASE_URL += "/?access_token={token}".format(
            token=CODECOV_API_TOKEN)
    resp = requests.get(CODECOV_BASE_URL)
    if resp.status_code != 200:
        raise Exception(
            "Unable to retrieve Codecov data (status_code={status_code}). "
            "Please check the following settings : "
            "CODECOV_SERVICE, CODEDOV_USERNAME and CODECOV_API_TOKEN if your "
            "repository is private.".format(resp.status_code))
    elif resp.json()["reason"] == u'No report found':
        raise Exception(
            "Unable to retrieve Codecov report. Are you sure to have "
            "activated Codecov report to the {repo} repository ?".format(
                repo=CODECOV_REPO_NAME))
