from django.shortcuts import render

# Create your views here.

def home(request):
    previous = ""

    return render(request, 'appHomePage/home.html', locals())
