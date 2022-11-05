import os

from scripts.tif_env import TEMP_PATH


def template_init():
    print('action_templates >> template_init >> chdir')
    os.chdir(TEMP_PATH)
