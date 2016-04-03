from django.utils import timezone

from decimal import Decimal
import requests

from . import settings
from ... import models
from ... import app_settings


class CodecovDataRetriever(object):

    def __init__(self, datetime=timezone.now()):

        resp = requests.get(settings.CODECOV_BASE_URL)
        report = resp.json()["report"]

        models.Codecov.objects.create(
            coverage=report["coverage"],
            hit=report["totals"]["hit"],
            partial=report["totals"]["partial"],
            branches=report["totals"]["branches"],
            lines=report["totals"]["lines"],
            missed=report["totals"]["missed"],
            files=len(report["files"].keys()),
            datetime=datetime)

        for app_name in app_settings.FOLLOWED_APPS:
            hit = 0
            partial = 0
            branches = 0
            lines = 0
            missed = 0
            files = 0
            round_ = Decimal(".01")

            for filename, filereport in report["files"].items():
                if filename.startswith(app_name):
                    hit += filereport["totals"]["hit"]
                    partial += filereport["totals"]["partial"]
                    branches += filereport["totals"]["branches"]
                    lines += filereport["totals"]["lines"]
                    missed += filereport["totals"]["missed"]
                    files += 1

            models.Codecov.objects.create(
                coverage=Decimal(float(hit)/lines).quantize(round_),
                hit=hit,
                partial=partial,
                branches=branches,
                lines=lines,
                missed=missed,
                files=files,
                app_name=app_name,
                datetime=datetime)
