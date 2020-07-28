from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from torrentfy.views import DashboardView


urlpatterns = [
    url(r'^index/$', DashboardView.as_view(), name='dashboard'),
]
