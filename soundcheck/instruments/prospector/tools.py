import json
import subprocess

from django.utils import timezone

from . import settings
from ... import models
from ... import app_settings


class ProspectorDataRetriever(object):

    def __init__(self, datetime=timezone.now()):

        p = subprocess.Popen(["prospector", "--output-format", "json",
                              "--uses",  "django", "--strictness",
                              settings.PROSPECTOR_STRICTNESS],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        data = json.loads(out)

        models.Prospector.objects.create(
            nb_messages=data["summary"]["message_count"],
            datetime=datetime)

        for app_name in app_settings.FOLLOWED_APPS:
            nb_app_messages = 0
            for message in data["messages"]:
                if message["location"]["path"].startswith(app_name):
                    nb_app_messages += 1

            models.Prospector.objects.create(
                nb_messages=nb_app_messages,
                app_name=app_name,
                datetime=datetime)
