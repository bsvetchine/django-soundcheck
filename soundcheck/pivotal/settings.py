from django.conf import settings

import requests


PIVOTAL_API_TOKEN = getattr(settings, "PIVOTAL_API_TOKEN")
PIVOTAL_PROJECT_ID = getattr(settings, "PIVOTAL_PROJECT_ID")
PIVOTAL_STORIES_FILTER = getattr(
    settings, "PIVOTAL_STORIES_FILTER",
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
