from django.contrib import admin
from blog.models import Post, BlogComment
# Register your models here.
admin.site.register((BlogComment))
admin.site.register((Post))

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('tinyInject.js',)

