from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from torrentfy.forms import SignupForm


class DashboardView(View):
    def get(self, request):
        return render(request,'inicio/index.html')


class TelaCadastroView(View):
    def get(self, request):
        return render(request, 'inicio/telacadastro.html')


class CadastroView(generic.CreateView):
        form_class = SignupForm
        success_url = reverse_lazy('dashboard')
        template_name = 'inicio/telacadastro.html'
