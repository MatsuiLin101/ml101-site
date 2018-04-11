from django.shortcuts import render
from bs4 import BeautifulSoup

import requests

# Create your views here.

def home(request):
    news_list = []

    url_Apple = "https://tw.appledaily.com/recommend/realtime"
    res_Apple = requests.get(url_Apple)
    soup_Apple = BeautifulSoup(res_Apple.text, "html.parser")
    news_Apple = soup_Apple.select(".item")
    for news in news_Apple:
        # new = (title, url, img, source)
        new = (news.find("img").get("alt"), news.find("a").get("href"), news.find("img").get("data-src"), "蘋果日報")
        news_list.append(new)

    return render(request, 'appNews/home.html', locals())
