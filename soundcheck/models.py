from . import app_settings

if app_settings.ENABLE_GIT:
    from .instruments.git.models import *
