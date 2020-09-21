from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from .forms import BlogPostModelForm
from .forms import RSContactForm
from .models import RSBlogPost

# CRUD

# GET -> Retrieve / List
# POST -> Create / Update / DELETE

# Create Retrieve update Delete (CRUD)


def rsblog_post_contact_view(request):
    form = RSContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RSContactForm()
    context = {
        "title": "Let's Talk Adventure",
        "form": form
    }
    return render(request, "form_studio.html", context)


def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = RSBlogPost.objects.all().published()  # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = RSBlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'rs_blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(RSBlogPost, slug=slug)
    template_name = 'rs_blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(RSBlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'rs_blog/form.html'
    context = {"title": f"Update {obj.title}", 'form': form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(RSBlogPost, slug=slug)
    template_name = 'rs_blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/rs-blog")
    context = {"object": obj}
    return render(request, template_name, context)
