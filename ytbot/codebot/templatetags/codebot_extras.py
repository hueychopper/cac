from django import template
from difflib import SequenceMatcher
import json
import requests
from bs4 import BeautifulSoup

register = template.Library()

@register.simple_tag
def pack_props(tr, ti, url):
    # print(ti)
    if len(ti) == len(url):
        return tuple(zip(tr, ti, url))

@register.simple_tag
def return_scripts(tup):
    return tup[0]

@register.simple_tag
def flag_text(transcript): # is array
    base = "sponsor"
    interests = []
    pred = ""
    res = {
        'interests': [],
        'pred': ''
    }
    if len(transcript) > 0:
        # print(len(transcript))
        for text in transcript:
            for word in text.split(" "):
                r = SequenceMatcher(None, base, word).ratio()
                # print("word: ", word, ", and ratio: ", r)
                if r >= 0.7:
                    print("WORD FOUND: ", word, " ratio: ", r)
                    interests.append(text)
                    pred = str("flagged: " + str(r*100) + "%")
                    # res["interests"] = interests
                    # res["pred"] = pred
                # else:
                #     print(r)
                #     pred = "No matches found"
                #     interests = []

        # print(tuple([pred,interests]))
        return [pred, interests]
    else:
        print("ERROR: transcript dne")
        return ['None', 'No transcripts']

@register.simple_tag
def getlen(arr):
    return len(arr)


@register.simple_tag
def get_desc(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')

    desc = soup.find("meta", itemprop="description")["content"]

    return desc

