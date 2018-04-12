from django.shortcuts import render
from bs4 import BeautifulSoup

import requests

# Create your views here.

def home(request):
    news_list = []
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    # Apple Daily News
    url_Apple = "https://tw.appledaily.com/recommend/realtime"
    res_Apple = requests.get(url_Apple)
    soup_Apple = BeautifulSoup(res_Apple.text, "html.parser")
    news_Apple = soup_Apple.select(".item")
    for apple in news_Apple:
        # new = (title, url, img, source)
        news = (apple.find("img").get("alt"), apple.find("a").get("href"), apple.find("img").get("data-src"), "蘋果日報")
        news_list.append(news)

    # Yahoo News
    url_Yahoo = "https://tw.news.yahoo.com/"
    res_Yahoo = requests.get(url_Yahoo, headers=headers)
    soup_Yahoo = BeautifulSoup(res_Yahoo.text, "html.parser")
    news_Yahoo = soup_Yahoo.find_all("img")
    atag_Yahoo = soup_Yahoo.find_all("a")
    for yahoo in news_Yahoo:
        if str(yahoo.get("style"))[0:17] == "object-fit:cover;" and str(yahoo.get("alt"))[0] == "/":
            if str(yahoo.get("style")) != "object-fit:cover;":
                start = str(yahoo.get("style")).find("http")
                end = str(yahoo.get("style")).find(");")
                img = str(yahoo.get("style"))[start:end]
            else:
                img = str(yahoo.get("src"))

            for atag in atag_Yahoo:
                if atag.get("href") == yahoo.get("alt"):
                    title = atag.text
                    break

            # new = (title, url, img, source)
            news = (title, "https://tw.news.yahoo.com" + yahoo.get("alt"), img, "Yahoo新聞")
            news_list.append(news)

    return render(request, 'appNews/home.html', locals())
