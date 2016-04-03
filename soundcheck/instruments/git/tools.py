import os.path
import os.walk

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

        files = []
        directories = []
        for root, directories, filenames in os.walk(git_repo_path):
            for directory in directories:
                directories.append(os.path.join(root, directory))
            for filename in filenames:
                files.append(os.path.join(root, filename))

        nb_lines = 0
        for file in files:
            with open(file) as f:
                nb_lines += sum(1 for _ in f)

        models.Git.objects.create(
            nb_lines=nb_lines,
            nb_files=len(files),
            nb_directories=len(directories),
            nb_commits=repo.commit(git_main_branch).count(),
            datetime=datetime
        )

        for app_name in app_settings.FOLLOWED_APPS:
            app_dir_pth = os.path.join(git_repo_path, app_name)
            app_directories = [dir_pth for dir_pth in directories
                               if dir_pth.startswith(app_dir_pth)]
            app_files = [file_pth for file_pth in files
                         if file_pth.startswith(app_dir_pth)]
            app_nb_lines = 0
            for file in app_files:
                with open(file) as f:
                    app_nb_lines += sum(1 for _ in f)

            models.Git.objects.create(
                nb_lines=app_nb_lines,
                nb_files=len(app_files),
                nb_directories=len(app_directories),
                nb_commits=repo.commit(git_main_branch).count(app_name),
                app_name=app_name,
                datetime=datetime)
