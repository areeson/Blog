from django.contrib import admin
from .models import Category
# Register your models here.
from .models import BlogPost


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(BlogPost)
