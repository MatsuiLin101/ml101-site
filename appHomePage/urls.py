from django.urls import path
from . import views

app_name = 'appHomePage'

urlpatterns = [
    path('', views.home, name='home')
]
