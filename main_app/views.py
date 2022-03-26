from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import FigureModels
from django.views.generic.edit import CreateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class ModelList(TemplateView):
    template_name = 'modellist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["models"] = FigureModels.objects.filter(name__icontains=name)
            context["header"] = f"Searching For {name}"
        else:
            context["models"] = FigureModels.objects.all()
            context["header"] = "Our Models"
        return context

class Model_Create(CreateView):
    model = FigureModels
    fields = ['name', 'img', 'brand', 'grade']
    template_name = "model_create.html"
    success_url = "/models/"
