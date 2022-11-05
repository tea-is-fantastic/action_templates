import os

from scripts.tif_yaml import app_yaml
from scripts.tif_env import TEMP_PATH, OUTPUT_PATH, GITHUB_TOKEN
import shutil


def template_exit():
    print('action_templates >> template_exit >> move')
    shutil.rmtree(OUTPUT_PATH, ignore_errors=True)
    os.mkdir(OUTPUT_PATH)

    file_names = os.listdir(TEMP_PATH)

    for file_name in file_names:
        shutil.move(os.path.join(TEMP_PATH, file_name), OUTPUT_PATH)

    print('action_templates >> template_exit >> git')
    repo_path = f"https://{GITHUB_TOKEN}@github.com/{app_yaml.repo}"

    os.chdir(os.path.join(OUTPUT_PATH, app_yaml.name))
    os.system('git config --global user.email "tif@replyqa.com"')
    os.system('git config --global user.name "Tea Is Fantastic"')
    os.system("git init .")
    os.system("git add -A")
    os.system('git commit -am "Initial commit"')
    os.system('git branch -M main')
    os.system(f'git remote add origin {repo_path}')
    os.system("git push --all -f")
