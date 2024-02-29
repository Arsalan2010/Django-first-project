
from django.shortcuts import render
from django.views.generic import TemplateView

class Message_View(TemplateView):
    
    template_name = "Home.html"