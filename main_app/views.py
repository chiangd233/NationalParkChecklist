from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .models import Park
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


class ParkList(TemplateView):
    template_name = "nationalpark.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["parks"] = Park.objects.all()
        return context