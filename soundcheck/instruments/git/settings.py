from django.conf import settings


# User configurable settings

GIT_REPO_PATH = getattr(settings, "GIT_REPO_PATH", None)
GIT_MAIN_BRANCH = getattr(settings, "GIT_MAIN_BRANCH", "master")
ENABLE_GIT = True if GIT_REPO_PATH else False


# Internal settings and install check

if ENABLE_GIT:
    try:
        import git
    except ImportError:
        raise ImportError("You must install python GitPython "
                          "(pip install gitpython) to retrieve repository "
                          "data.")
