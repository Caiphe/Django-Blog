from django.contrib import admin
from .models import Post


class PostDsiplay(admin.ModelAdmin):
    list_display = ('author', 'title',  'date_posted')


admin.site.register(Post, PostDsiplay)
