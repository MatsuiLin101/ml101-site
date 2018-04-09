from django.shortcuts import render, redirect
from bs4 import BeautifulSoup

import requests

# Create your views here.

def home(request):

    if request.method == "POST":
        url = request.POST.get("href")

        # Check url is under ptt domain
        if url[0:22] != "https://www.ptt.cc/bbs":
            url = "https://www.ptt.cc/bbs/" + url + "/index.html"

        if "index" in url:
            tag = 0
        else:
            tag = 1

        html = requests.get(url, cookies={"over18":"1"})
        html.decoding = "utf-8"

        if html.status_code != 200:
            message = "輸入錯誤或查無此看板、文章，請重新輸入。"

            return render(request, 'appPttParser/home.html', {"message":message})

        soup = BeautifulSoup(html.text, 'html.parser')
        soup_list = soup.find_all("a")
        image_list = []

        if tag == 0:
            for atag in soup_list:
                if "M." in str(atag.get("href")):
                    html = requests.get("https://www.ptt.cc" + str(atag.get("href")), cookies={"over18":"1"})
                    html.decoding = "utf-8"
                    soup = BeautifulSoup(html.text, "html.parser")
                    image_list.append(soup.title.text)
                    img_tag = soup.find_all("a")
                    for img in img_tag:
                        if ".jpg" in str(img.get("href")) or ".png" in str(img.get("href")):
                            image_list.append(str(img.get("href")))
        else:
            image_list.append(soup.title.text)
            for atag in soup_list:
                image_href = str(atag.get("href"))
                if ".jpg" in image_href or ".png" in image_href:
                    image_list.append(image_href)

        return render(request, 'appPttParser/show_img.html', locals())

    return render(request, 'appPttParser/home.html', locals())

def show_img(request):

    return render(request, 'appPttParser/show_img.html')
