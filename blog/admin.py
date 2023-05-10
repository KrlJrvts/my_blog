from django.contrib import admin
from blog.models import BlogPost


# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(BlogPost, BlogAdmin)


