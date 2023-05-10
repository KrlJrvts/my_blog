from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View
from .models import BlogPost


# Create your views here.

class AllBlogPosts(ListView):
    template_name = 'elements/main/all_posts.html'
    model = BlogPost


class SingleBlogPost(DetailView):
    template_name = 'elements/main/single_post.html'
    model = BlogPost


class CreateBlogPost(CreateView):
    template_name = 'elements/main/create_post.html'
    model = BlogPost
    fields = ['title', 'paragraph', 'author_name']


class DeleteBlogPost(View):
    def get(self, request, post_id):
        post = BlogPost.objects.get(id=post_id)
        post.delete()
        return render(request, 'elements/main/all_posts.html')


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
