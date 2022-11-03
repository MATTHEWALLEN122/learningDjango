from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "Hello there..."
    context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)

def about(request):
    my_title = "About us..."
    context = {"title": my_title, }
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": ['a', 'b', 'c', 'd', 'e']}
    return render(request, "hello_world.html", context)

def contact(request):
    my_title = "Contact Us..."
    return render(request, "hello_world.html", {"title": my_title})

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)