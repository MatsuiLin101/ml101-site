from django.urls import path
from . import views

app_name = "appNews"

urlpatterns = [
    path('', views.home, name='home'),
]
