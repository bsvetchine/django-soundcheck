from django.conf import settings


# User configurable settings

PROSPECTOR_PROJECT_PATH = getattr(settings, "PROSPECTOR_PROJECT_PATH", None)
PROSPECTOR_STRICTNESS = getattr(settings, "PROSPECTOR_STRICTNESS", "medium")


# Internal settings and install check

ENABLE_PROSPECTOR = True if PROSPECTOR_PROJECT_PATH else False

if ENABLE_PROSPECTOR:
    try:
        import prospector
    except ImportError:
        raise ImportError("You must install python prospector "
                          "(pip install prospector) to lint project.")
