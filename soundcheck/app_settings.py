import base64

from django.conf import settings

import requests


# Django project related settings

FOLLOWED_APPS = settings.get("FOLLOWED_APPS", ())


# Git related settings

GIT_REPO_PATH = settings.get("GIT_REPO_PATH")
GIT_MAIN_BRANCH = settings.get("GIT_MAIN_BRANCH", "master")
ENABLE_GIT = True if GIT_REPO_PATH else False

if ENABLE_GIT:
    try:
        import git
    except ImportError:
        raise ImportError("You must install python GitPython "
                          "(pip install gitpython) to retrieve repository "
                          "data.")


# Codecov related settings

CODECOV_SERVICE = settings.get("CODEDOV_SERVICE")
CODEDOV_USERNAME = settings.get("CODEDOV_USERNAME")
CODECOV_API_TOKEN = settings.get("CODECOV_API_TOKEN")
CODECOV_REPO_NAME = settings.get("CODEDOV_REPO_NAME")

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


# Sentry related settings

SENTRY_API_TOKEN = settings.get("SENTRY_API_TOKEN")
SENTRY_ORGANIZATION_SLUG = settings.get("SENTRY_ORGANIZATION_SLUG")
SENTRY_PROJECT_SLUG = settings.get("SENTRY_PROJECT_SLUG")

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


# Pivotal related settings

PIVOTAL_API_TOKEN = settings.get("PIVOTAL_API_TOKEN")
PIVOTAL_PROJECT_ID = settings.get("PIVOTAL_PROJECT_ID")
PIVOTAL_STORIES_FILTER = settings.get(
    "PIVOTAL_STORIES_FILTER",
    "state:delivered,finished,rejected,started,unstarted")

ENABLE_PIVOTAL = True if PIVOTAL_API_TOKEN and PIVOTAL_PROJECT_ID else False

if ENABLE_PIVOTAL:
    PIVOTAL_API_HEADERS = {"X-TrackerToken": PIVOTAL_API_TOKEN}
    PIVOTAL_API_URL = (
        "https://www.pivotaltracker.com/services/v5/projects/{project_id}/"
        "stories/?filter={filter}".format(
            project_id=PIVOTAL_PROJECT_ID,
            filter=PIVOTAL_STORIES_FILTER)
    )
    resp = requests.get(PIVOTAL_API_URL, headers=PIVOTAL_API_HEADERS)
    if not resp.status_code != 200:
        raise Exception(
            "Unable to retrive Pivotal data (status_code={status_code}). "
            "Please check the following settings : "
            "PIVOTAL_API_TOKEN, PIVOTAL_PROJECT_ID".format(
                status_code=resp.status_code))


# Zendesk related settings

ZENDESK_LOGIN = settings.get("ZENDESK_LOGIN")
ZENDESK_PASSWORD = settings.get("ZENDESK_PASSWORD")
ZENDESK_TICKET_STATUSES_FILTER = settings.get(
    "ZENDESK_TICKET_STATUSES_FILTER",
    ("new", "open", "pending", "hold"))

ENABLE_ZENDESK = True if ZENDESK_LOGIN and ZENDESK_PASSWORD else False

if ENABLE_ZENDESK:
    status_filter = ""
    for status in ZENDESK_TICKET_STATUSES_FILTER:
        status_filter += "+status%3A{status}".format(status=status)
    ZENDESK_API_URL = (
        "https://spicesoft.zendesk.com/api/v2/search.json?query=type%3Aticket"
        "{status_filter}".format(status_filter=status_filter)
    )
    resp = requests.get(ZENDESK_API_URL,
                        auth=(ZENDESK_LOGIN, ZENDESK_PASSWORD))
    if not resp.status_code != 200:
        raise Exception(
            "Unable to retrive Zendesk data (status_code={status_code}). "
            "Please check the following settings : "
            "ZENDESK_LOGIN, ZENDESK_PASSWORD and eventually "
            "ZENDESK_TICKET_STATUSES_FILTER".format(
                status_code=resp.status_code))
