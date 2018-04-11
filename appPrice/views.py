from django.shortcuts import render

import requests, json

# Create your views here.

def home(request):

    if request.method == "POST":
        item_name = request.POST.get("name")
        url_Pchome = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + item_name + "&page=1&sort=rnk/dc"
#        url_Yahoo =
        res_Pchome = requests.get(url_Pchome)
        data_Pchome = json.loads(res_Pchome.text)
        item_list = []
        if data_Pchome["totalRows"] != 0:
            item_Pchome = data_Pchome["prods"]
            for i in range(3 if data_Pchome["totalRows"] >= 3 else data_Pchome["totalRows"]):
                # item = (name, link, price, img, shop)
                item = (item_Pchome[i].get("name"), "https://24h.pchome.com.tw/prod/" + item_Pchome[i].get("Id"), item_Pchome[i].get("price"), "https://a.ecimg.tw" + item_Pchome[i].get("picS"), "PChome24h購物")
                item_list.append(item)

        return render(request, 'appPrice/result.html', locals())

    return render(request, 'appPrice/home.html')
