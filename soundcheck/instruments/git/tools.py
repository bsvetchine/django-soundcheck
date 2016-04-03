import os

from django.utils import timezone

from git import Repo

from . import settings
from ... import models
from ... import app_settings


class GitDataRetriever(object):

    def __init__(self, datetime=timezone.now()):

        git_repo_path = settings.GIT_REPO_PATH
        repo = Repo(git_repo_path)
        git_main_branch = settings.GIT_MAIN_BRANCH

        git_files = []
        git_dirs = []
        for root, dirs, files in os.walk(git_repo_path):
            for git_dir in [d for d in dirs if not d[0] == '.']:
                git_dirs.append(os.path.join(root, git_dir))
            for git_file in [f for f in files if not f[0] == '.']:
                git_files.append(os.path.join(root, git_file))

        nb_lines = 0
        for git_file in git_files:
            with open(git_file) as f:
                nb_lines += sum(1 for _ in f)

        models.Git.objects.create(
            nb_lines=nb_lines,
            nb_files=len(git_files),
            nb_dirs=len(git_dirs),
            nb_commits=repo.commit(git_main_branch).count(),
            datetime=datetime
        )

        for app_name in app_settings.FOLLOWED_APPS:
            app_dir_pth = os.path.join(git_repo_path, app_name)
            app_directories = [dir_pth for dir_pth in git_dirs
                               if dir_pth.startswith(app_dir_pth)]
            app_files = [file_pth for file_pth in git_files
                         if file_pth.startswith(app_dir_pth)]
            app_nb_lines = 0
            for file in app_files:
                with open(file) as f:
                    app_nb_lines += sum(1 for _ in f)

            models.Git.objects.create(
                nb_lines=app_nb_lines,
                nb_files=len(app_files),
                nb_dirs=len(app_directories),
                nb_commits=repo.commit(git_main_branch).count(app_name),
                app_name=app_name,
                datetime=datetime)
