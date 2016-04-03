from django.conf import settings

from .codecov.settings import ENABLE_CODECOV
from .git.settings import ENABLE_GIT
from .pivotal.settings import ENABLE_PIVOTAL
from .prospector.settings import ENABLE_PROSPECTOR
from .sentry.settings import ENABLE_SENTRY
from .zendesk.settings import ENABLE_ZENDESK


FOLLOWED_APPS = getattr(settings, "FOLLOWED_APPS", ())
