from django.conf import settings

import requests


# User configurable settings

ZENDESK_LOGIN = getattr(settings, "ZENDESK_LOGIN", None)
ZENDESK_PASSWORD = getattr(settings, "ZENDESK_PASSWORD", None)
ZENDESK_TICKET_STATUSES_FILTER = getattr(
    settings, "ZENDESK_TICKET_STATUSES_FILTER",
    ("new", "open", "pending", "hold"))


# Internal settings and connection check

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
