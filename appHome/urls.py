from django.urls import path
from . import views

app_name = 'appHome'

urlpatterns = [
    path('', views.home, name='home')
]