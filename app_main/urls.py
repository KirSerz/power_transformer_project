from django.conf.urls import url, include
from app_main.views import BasePage

urlpatterns = [
    url(r'^base_page/$', BasePage.as_view())
]