from django.urls import path
from . import views

app_name = 'appPttParser'

urlpatterns = [
    path('', views.home, name='home')
]
