from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
class AboutPage(TemplateView):
    template_name = 'about.html'
class Base(TemplateView):
    template_name = 'base.html'