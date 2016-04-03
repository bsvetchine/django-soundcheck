from django.utils import timezone

import requests

from . import settings
from ... import models
from ... import app_settings


class ZendeskDataRetriever(object):

    def identify_tickets(self, tickets):
        nb_tickets_by_priority = {"urgent": 0, "high": 0, "normal": 0,
                                  "low": 0, None: 0}
        nb_tickets_by_status = {"new": 0, "open": 0, "pending": 0, "hold": 0}

        for ticket in tickets:
            nb_tickets_by_priority[ticket["priority"]] += 1
            nb_tickets_by_status[ticket["status"]] += 1
        return nb_tickets_by_priority, nb_tickets_by_status

    def __init__(self, datetime=timezone.now()):

        resp = requests.get(
            settings.ZENDESK_API_URL,
            auth=(settings.ZENDESK_LOGIN, settings.ZENDESK_PASSWORD))

        tickets = resp.json()["results"]
        nb_tickets_by_priority, nb_tickets_by_status = self.identify_tickets(
            tickets)

        models.Zendesk.objects.create(
            nb_tickets=len(tickets),
            nb_urgent_tickets=nb_tickets_by_priority["urgent"],
            nb_high_tickets=nb_tickets_by_priority["high"],
            nb_normal_tickets=nb_tickets_by_priority["normal"],
            nb_low_tickets=nb_tickets_by_priority["low"],
            nb_new_tickets=nb_tickets_by_status["new"],
            nb_open_tickets=nb_tickets_by_status["open"],
            nb_pending_tickets=nb_tickets_by_status["pending"],
            nb_hold_tickets=nb_tickets_by_status["hold"],
            datetime=datetime)

        for app_name in app_settings.FOLLOWED_APPS:
            app_tickets = []
            for ticket in tickets:
                if app_name in ticket["tags"]:
                    app_tickets.append(ticket)

            nb_stories_by_type, nb_stories_by_state = self.identify_tickets(
                app_tickets)

            models.Zendesk.objects.create(
                nb_tickets=len(app_tickets),
                nb_urgent_tickets=nb_tickets_by_priority["urgent"],
                nb_high_tickets=nb_tickets_by_priority["high"],
                nb_normal_tickets=nb_tickets_by_priority["normal"],
                nb_low_tickets=nb_tickets_by_priority["low"],
                nb_new_tickets=nb_tickets_by_status["new"],
                nb_open_tickets=nb_tickets_by_status["open"],
                nb_pending_tickets=nb_tickets_by_status["pending"],
                nb_hold_tickets=nb_tickets_by_status["hold"],
                app_name=app_name,
                datetime=datetime)
