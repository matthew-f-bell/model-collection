from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Figure, Paint
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.models import User

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Model_List(TemplateView):
    template_name = 'model_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["figures"] = Figure.objects.filter(name__icontains=name)
            context["header"] = f"Searching For {name}"
        else:
            context["figures"] = Figure.objects.all()
            context["header"] = "Our Models"
        return context

class Model_Create(CreateView):
    model = Figure
    fields = ['name', 'img', 'brand', 'grade', 'user']
    template_name = 'model_create.html'
    # success_url = "/models/"
    # def get_success_url(self):
    #     return reverse('model_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/models/')

class Model_Detail(DetailView):
    model = Figure
    template_name = 'model_detail.html'


class Model_Update(UpdateView):
    model = Figure
    fields = ['name', 'img', 'brand', 'grade']
    template_name = 'model_update.html'
    # success_url = "/models/"
    def get_success_url(self):
        return reverse('model_detail', kwargs={'pk': self.object.pk})

class Model_Delete(DeleteView):
    model = Figure
    template_name = "model_delete_confirmation.html"
    success_url = "/models/"

# user profile
def profile(request, username):
    user = User.objects.get(username=username)
    figures = Figure.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'figures':figures})

def paint_list(request):
    paints = Paint.objects.all()
    return render(request, 'paint_show.html', {'paints': paints})

def paint_detail(request, paint_id):
    paint = Paint.objects.get(id=paint_id)
    return render(request, 'paint_show.html', {'paint': paint})

class Paint_Create(CreateView):
    model = Paint
    fields = '__all__'
    template_name = 'paint_create.html'
    success_url = '/paints'

class Paint_Update(UpdateView):
    model = Paint
    fields = ['color', 'paint_type']
    template_name = "paint_update.html"
    success_url = "/paints"

class Paint_Delete(DeleteView):
    model = Paint
    template_name = "paint_delete_confirmation.html"
    success_url = '/paints'

