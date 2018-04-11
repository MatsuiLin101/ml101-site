from django.shortcuts import render
from bs4 import BeautifulSoup

import requests, json

# Create your views here.

def home(request):

    if request.method == "POST":
        item_name = request.POST.get("name")
        item_list = []

        # PChome
        url_Pchome = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + item_name + "&page=1&sort=rnk/dc"
        res_Pchome = requests.get(url_Pchome)
        data_Pchome = json.loads(res_Pchome.text)
        if data_Pchome["totalRows"] != 0:
            item_Pchome = data_Pchome["prods"]
            for i in range(3 if data_Pchome["totalRows"] >= 3 else data_Pchome["totalRows"]):
                # item = (name, link, price, img, shop)
                item = (
                    item_Pchome[i].get("name"),
                    "https://24h.pchome.com.tw/prod/" + item_Pchome[i].get("Id"),
                    "$" + str(item_Pchome[i].get("price")),
                    "https://a.ecimg.tw" + item_Pchome[i].get("picS"),
                    "PChome24h購物"
                )
                item_list.append(item)

        # Yahoo
        url_Yahoo = "https://tw.search.buy.yahoo.com/search/shopping/product?p=" + item_name + "&qt=product&cid=0&clv=0&cid_path="
        res_Yahoo = requests.post(url_Yahoo)
        soup = BeautifulSoup(res_Yahoo.text, "html.parser")
        data_Yahoo = soup.select(".BaseGridItem__content___3LORP")
        if len(data_Yahoo) != 0:
            for i in range(3 if len(data_Yahoo) >= 3 else len(data_Yahoo)):
                item = (
                    data_Yahoo[i].text.split("$")[0],
                    data_Yahoo[i].get("href"),
                    "$" + data_Yahoo[i].text.split("$")[1] if not "折" in data_Yahoo[i].text else "$" + data_Yahoo[i].text.split("$")[1].split("折")[0],
#                    data_Yahoo[i].text,
                    data_Yahoo[i].find_all("div")[0].get("style").split("(")[1].split(")")[0],
                    "Yahoo購物中心"
                )
                item_list.append(item)

        return render(request, 'appPrice/result.html', locals())

    return render(request, 'appPrice/home.html')
