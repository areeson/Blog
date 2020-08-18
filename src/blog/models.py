from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

# Don't forget three things for CHANGES TO THIS FILE:
# 1. Make sure the app is in your settings
# 2. python manage.py makemigrations
# 3. python manage.py migrate

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = BlogPostManager()

    class Meta:
        ordering = ['publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"/blog/{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"/blog/{self.get_absolute_url()}/delete"
