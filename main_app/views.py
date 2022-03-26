from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Model: 
        def __init__(self, brand, name, grade):
            self.brand = brand
            self.name = name
            self.grade = grade

models = [
    Model("Bandai", "Wukong Impulse", "SD Gundam"),
    Model("Bandai", "DeathScythe Hell", "MG"),
    Model("Bandai", "RX-78GP01 Gundam", "HG"),
    Model("Bandai", "Pikachu (Battle Pose)", "No Grade"),
]

class ModelList(TemplateView):
    template_name = 'modellist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = models
        return context
