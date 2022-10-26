import os
from pathlib import Path
from difflib import SequenceMatcher
from urllib.parse import urlparse

def matchdriver(browser_name):
    cwd, pcwd = os.getcwd(), Path.cwd()
    wd_dir = pcwd.joinpath('codebot/webdrivers/')

    for browser in wd_dir.iterdir():
        seq = SequenceMatcher(None, browser_name, str(browser).split("/")[-1]).ratio()
        if seq >= 0.7:
            current_driver = [str(driver) for driver in browser.iterdir()]
            return current_driver[0]

