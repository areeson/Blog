from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost
from rs_blog.models import RSBlogPost
# Don't Repeat Yourself = DRY
# Below the functions are used to allow for parent/child


# ---------------------------------------
# Home Page
def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Andrew Reeson", 'blog_list': qs}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


# this is currently acting as the reeson tech contact page, there is no contact page on the home page yet.
def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
    context = {
        "title": "Message Me",
        "form": form
    }
    return render(request, "form.html", context)


# ---------------------------------------
# Reeson Tech
def reesontech_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Andrew Reeson", 'blog_list': qs}
    return render(request, "reesontech.html", context)


def rtabout_page(request):
    return render(request, "about_tech.html", {"title": "About Us"})

# this is not in use yet, this will be what the contact page for the home page above is right now.


def rtcontact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Message Me RT",
        "form": form
    }
    return render(request, "form_tech.html", context)


# ---------------------------------------
# Reeson Studio
def reesonstudio_page(request):
    qs = RSBlogPost.objects.all()[:5]
    context = {"title": "Andrew Reeson", 'blog_list': qs}
    return render(request, "reesonstudio.html", context)


def rscontact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Message Me",
        "form": form
    }
    return render(request, "form_studio.html", context)


def rsabout_page(request):
    return render(request, "about_studio.html", {"title": "About Us"})


def gallery_page(request):
    return render(request, "gallery.html", {"title": "Gallery"})
