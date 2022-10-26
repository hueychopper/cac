from django import template
from difflib import SequenceMatcher

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
    if len(transcript) > 0:
        for text in transcript:
            for word in text.split(" "):
                r = SequenceMatcher(None, base, word).ratio()
                if r > 0.79:
                    interests.append(text)
                    pred = str("flagged: " + str(r*100) + "%")

        print(tuple([pred,interests]))
        return tuple([pred,interests])

@register.simple_tag
def to_str_n(var):
    return (str(var)+"\n")