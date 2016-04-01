from django.conf import settings


FOLLOWED_APPS = settings.get("FOLLOWED_APPS", ())

GIT_REPO_PATH = settings.get("GIT_REPO_PATH", None)

GIT_MAIN_BRANCH = settings.get("GIT_MAIN_BRANCH", "master")

ENABLE_GIT = True if GIT_REPO_PATH else False

if ENABLE_GIT:
    try:
        import git
    except ImportError:
        raise ImportError("You must install python GitPython "
                          "(pip install gitpython) to retrieve repository "
                          "data.")
