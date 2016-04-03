from django.conf import settings

from .instruments.codecov.settings import ENABLE_CODECOV
from .instruments.git.settings import ENABLE_GIT
from .instruments.pivotal.settings import ENABLE_PIVOTAL
from .instruments.prospector.settings import ENABLE_PROSPECTOR
from .instruments.sentry.settings import ENABLE_SENTRY
from .instruments.zendesk.settings import ENABLE_ZENDESK


FOLLOWED_APPS = getattr(settings, "FOLLOWED_APPS", ())
