from django.shortcuts import render,get_list_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

def paginator(request):
    categories = Category_mst.objects.all()
    all_post = Paginator(Service_mst.objects.filter(available = True),3)
    page = request.GET.get('page')
    try:
	    posts = all_post.page(page)
    except PageNotAnInteger:
	    posts = all_post.page(1)
    except EmptyPage:
	    posts = all_post.page(all_post.num_pages)
    return render(request, 'ad-list-view.html', 
                    {'posts': posts,
                       'categories':categories,
                    }) 

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