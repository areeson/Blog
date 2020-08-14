from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Don't Repeat Yourself = DRY
# Below the functions are used to allow for parent/child


def home_page(request):
    my_title = "Hello there...."
    context = {"title": "my title"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    return render(request, "contact_us.html", {"title": "Contact Us"})


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))
