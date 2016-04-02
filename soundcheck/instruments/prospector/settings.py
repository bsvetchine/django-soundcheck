from django.conf import settings


PROSPECTOR_PROJECT_PATH = settings.get("PROSPECTOR_PROJECT_PATH")
PROSPECTOR_STRICTNESS = settings.get("PROSPECTOR_STRICTNESS", "medium")

ENABLE_PROSPECTOR = True if PROSPECTOR_PROJECT_PATH else False

if ENABLE_PROSPECTOR:
    try:
        import prospector
    except ImportError:
        raise ImportError("You must install python prospector "
                          "(pip install prospector) to lint project.")
