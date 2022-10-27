import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.chrome.options
import selenium.webdriver.firefox.options 
import selenium.webdriver.opera.options
import sys
import environ
import json
import requests
from youtube_transcript_api import YouTubeTranscriptApi
import os


env = environ.Env()
environ.Env.read_env()
def get_tr(id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(str(id))
    except:
        transcript = None
    formatted = []
    if transcript != None:
        for dict in transcript:
            for key, val in dict.items():
                if key == "text":
                    formatted.append(val.replace("\n", " "))
    else:
        formatted.append("No transcript")
    return formatted

def useDriver(name, dir, input_url, mr=10):
    if name == "Firefox":
        b_opts = selenium.webdriver.firefox.options.Options()
        b_opts.add_argument("--headless")
        wd = webdriver.Firefox(executable_path=dir,options=b_opts)
    elif name == "Chrome":
        b_opts = selenium.webdriver.chrome.options.Options()
        b_opts.add_argument("--headless")
        wd = webdriver.Chrome(executable_path=dir,options=b_opts)
    elif name == "Opera":
        b_opts = selenium.webdriver.opera.options.Options()
        b_opts.add_argument("--headless")
        wd = webdriver.Opera(executable_path=dir,options=b_opts)
    else:
        print(name)

    url = str(input_url) + "/videos"
    wd.get(url)
    time.sleep(5)
    allvids = wd.find_elements(By.XPATH, "//*[@id='video-title']")
    # titles, urls = [], []
    if mr <= 30:
        titles = [i.get_attribute("aria-label") for i in allvids]
        urls = [str(i.get_attribute("href")) for i in allvids]
        ids = [url.split("=")[-1] for url in urls]
        return ids[:mr], titles[:mr], urls[:mr]
    else:
        ids = [str(i.get_attribute("href")).split("=")[1] for i in allvids]
        prev_height = wd.execute_script("return document.documentElement.scrollHeight")
        while len(ids) != mr:
            if len(ids) == mr:
                print(ids)
                break
            else:
                wd.execute_script(f"window.scrollTo(0, {prev_height});")
                time.sleep(1.2)
                nthvids = wd.find_elements(By.XPATH, "//*[@id='video-title']")
                if len(nthvids) >= mr:
                    titles = [i.get_attribute("aria-label") for i in allvids]
                    urls = [str(i.get_attribute("href")) for i in allvids]
                    ids = [str(i.get_attribute("href")).split("=")[1] for i in nthvids]
                    break
                new_height = wd.execute_script("return document.documentElement.scrollHeight")
                if new_height == prev_height:
                    break

                prev_height = new_height

        return ids[:mr], titles[:mr], urls[:mr]

def tr_driver(name, dir, input_url, mr=10):
    base = useDriver(name, dir, input_url, mr)
    trs = [get_tr(id) for id in base[0]]
    return trs, base[1], base[2]


