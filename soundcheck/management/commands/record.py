# pylint: disable=no-self-use
# flake8: noqa
"""Record custom management command."""

from django.core.management.base import BaseCommand

from ... import app_settings


class Command(BaseCommand):
    """Listen all instruments and store data in database."""

    help = "Listen to all instruments and store data in database."

    def handle(self, *args, **options):
        """Call all enabled instruments tools to retrieve data."""
        self.stdout.write(u"record command started.")
        if app_settings.ENABLE_CODECOV:
            from soundcheck.instruments.codecov import tools
            tools.CodecovDataRetriever()
            self.stdout.write(u"  -> Codecov data recorded successfully.")
        if app_settings.ENABLE_GIT:
            from soundcheck.instruments.git import tools
            tools.GitDataRetriever()
            self.stdout.write(u"  -> Git data recorded successfully.")
        if app_settings.ENABLE_PIVOTAL:
            from soundcheck.instruments.pivotal import tools
            tools.PivotalDataRetriever()
            self.stdout.write(u"  -> Pivotal data recorded successfully.")
        if app_settings.ENABLE_PROSPECTOR:
            from soundcheck.instruments.prospector import tools
            tools.ProspectorDataRetriever()
            self.stdout.write(u"  -> Prospector data recorded successfully.")
        if app_settings.ENABLE_SENTRY:
            from soundcheck.instruments.sentry import tools
            tools.SentryDataRetriever()
            self.stdout.write(u"  -> Sentry data recorded successfully.")
        if app_settings.ENABLE_ZENDESK:
            from soundcheck.instruments.zendesk import tools
            tools.ZendeskDataRetriever()
            self.stdout.write(u"  -> Zendesk data recorded successfully.")
        self.stdout.write(u"record command ended.")
