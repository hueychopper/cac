# from lib2to3.pgen2 import driver
from pathlib import Path
import json
from django.shortcuts import render
from django.http import HttpResponse

from codebot.reqe import matchdriver
from codebot.useDriver import tr_driver

# Create your views here.
def main(req):
    dtu = matchdriver(req.user_agent.browser.family)
    query = req.GET.get('chn')
    mr = req.GET.get('maxResults')
    if query != None and query != "" and mr != "" and mr != None:
        driver_results = tr_driver(req.user_agent.browser.family, dtu, "https://youtube.com/c/"+str(query), int(mr))
        sample = {
            "UA": req.META['HTTP_USER_AGENT'],
            "browser_name": req.user_agent.browser.family,
            "query": query,
            "trs": driver_results[0],
            "titles": driver_results[1],
            "urls": driver_results[2],
        }
        jsonctx = json.dumps(sample)
        # print(jsonctx)
        sample['jctx'] = jsonctx
        return render(req, 'main.html', sample)
    else:
        driver_results = tr_driver(req.user_agent.browser.family, dtu, "https://youtube.com/c/"+str(query))
        sample = {
            "UA": req.META['HTTP_USER_AGENT'],
            "browser_name": req.user_agent.browser.family,
            "query": query,
            "trs": driver_results[0],   
            "titles": driver_results[1],
            "urls": driver_results[2]
        }
        jsonctx = json.dumps(sample)
        # print(jsonctx)
        sample['jctx'] = jsonctx
        return render(req, 'main.html', sample)


def about(req):
    return render(req, 'about.html')
def goDeep(req):
    return render(req, 'recs/deep.html')