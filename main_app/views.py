from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .models import Park
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


class ParkList(TemplateView):
    template_name = "nationalpark.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["parks"] = Park.objects.filter(name__icontains = name)
            context["header"] = f"Searching for {name.capitalize()}"
        else :
            context["parks"] = Park.objects.all()
            context["header"] = "All National Parks"
        return context

class Park_Create(CreateView):
    model = Park
    fields = ['name', 'state', 'size', 'birthday']
    template_name = "park_create.html"
    
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/parks')

class Park_Detail(DetailView):
    model = Park
    template_name = "park_detail.html"

class Park_Update(UpdateView):
    model = Park
    fields = ['name', 'state', 'size', 'birthday']
    template_name = "park_update.html"
    def get_success_url(self):
        return reverse('park_detail', kwargs = {'pk': self.object.pk})

class Park_Delete(DeleteView):
    model = Park
    template_name = "park_delete_confirm.html"
    success_url = "/parks/"

def profile(request, username):
    user = User.objects.get(username = username)
    parks = Park.objects.filter(user = user)
    return render(request, 'profile.html', {'username' : username, 'parks' : parks})