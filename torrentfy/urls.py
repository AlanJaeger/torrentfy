from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from torrentfy.views import DashboardView, TelaCadastroView


urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^cadastro/$', TelaCadastroView.as_view(), name='cadastro'),

]
