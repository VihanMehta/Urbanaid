from django.shortcuts import render,get_list_or_404
from django.views.generic import TemplateView
from .models import *

class servicesView(TemplateView):
    template_name="category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services_list'] = Service_mst.objects.all().order_by("-id")
        context['categories'] = Category_mst.objects.all()
        return context

class servicedetailsView(TemplateView):
    template_name="single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug=self.kwargs['slug']
        services_list= Service_mst.objects.get(slug=url_slug)
        data = Professional_mst.objects.all()
        stu = {"prof": data}
        context['services_list'] = services_list
        return context

# Create your views here.