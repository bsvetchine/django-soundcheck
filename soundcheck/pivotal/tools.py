from django.utils import timezone

import requests

from . import settings
from .. import models
from .. import app_settings


class PivotalDataRetriever(object):

    def identify_stories(self, stories):
        nb_stories_by_type = {"release": 0, "feature": 0, "bug": 0, "chore": 0}
        nb_stories_by_state = {"delivered": 0, "finished": 0, "rejected": 0,
                               "started": 0, "unstarted": 0}

        total_points = 0
        for story in stories:
            nb_stories_by_type[story["story_type"]] += 1
            nb_stories_by_state[story["current_state"]] += 1
            total_points += story["estimate"]
        return total_points, nb_stories_by_type, nb_stories_by_state

    def __init__(self, datetime=timezone.now()):

        resp = requests.get(
            settings.PIVOTAL_API_URL,
            headers=settings.PIVOTAL_API_HEADERS)

        stories = resp.json()
        total_points, nb_stories_by_type, nb_stories_by_state = (
            self.identify_stories(stories))

        models.Pivotal.objects.create(
            nb_stories=len(stories),
            total_points=total_points,
            nb_features=nb_stories_by_type["feature"],
            nb_bugs=nb_stories_by_type["bug"],
            nb_chores=nb_stories_by_type["chore"],
            nb_releases=nb_stories_by_type["release"],
            nb_delivered_stories=nb_stories_by_state["delivered"],
            nb_finished_stories=nb_stories_by_state["finished"],
            nb_rejected_stories=nb_stories_by_state["rejected"],
            nb_started_stories=nb_stories_by_state["started"],
            nb_unstarted_stories=nb_stories_by_state["unstarted"],
            datetime=datetime)

        for app_name in app_settings.FOLLOWED_APPS:
            app_stories = []
            for story in stories:
                for label in story["labels"]:
                    if label["name"] == app_name:
                        app_stories.append(story)

            total_points, nb_stories_by_type, nb_stories_by_state = (
                self.identify_stories(app_stories))

            models.Pivotal.objects.create(
                nb_stories=len(app_stories),
                total_points=total_points,
                nb_features=nb_stories_by_type["feature"],
                nb_bugs=nb_stories_by_type["bug"],
                nb_chores=nb_stories_by_type["chore"],
                nb_releases=nb_stories_by_type["release"],
                nb_delivered_stories=nb_stories_by_state["delivered"],
                nb_finished_stories=nb_stories_by_state["finished"],
                nb_rejected_stories=nb_stories_by_state["rejected"],
                nb_started_stories=nb_stories_by_state["started"],
                nb_unstarted_stories=nb_stories_by_state["unstarted"],
                app_name=app_name,
                datetime=datetime)
