from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View
from .models import BlogPost


class AllBlogPosts(ListView):
    template_name = 'all_posts.html'
    model = BlogPost


class SingleBlogPost(DetailView):
    template_name = 'single_post.html'
    model = BlogPost


class CreateBlogPost(CreateView):
    template_name = 'create_post.html'
    model = BlogPost
    fields = ['title', 'paragraph', 'author_name']


class DeleteBlogPost(View):
    def get(self, request, post_id):
        post = BlogPost.objects.get(id=post_id)
        post.delete()
        return render(request, 'all_posts.html')


class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')
