from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View



class DashboardView(View):
    def get(self, request):
        return render(request,'inicio/index.html')
# Create your views here.
