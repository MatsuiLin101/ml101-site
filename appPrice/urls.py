from django.urls import path
from . import views

app_name = 'appPrice'

urlpatterns = [
    path('', views.home, name='home'),
]
