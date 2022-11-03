from django.shortcuts import render

# Create your views here.

from .models import Blogpost



def blog_post_detail(request):
    obj = Blogpost.objects.get(id=2)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)