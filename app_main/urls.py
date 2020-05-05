from django.conf.urls import url, include
from app_main.views import BasePage
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]