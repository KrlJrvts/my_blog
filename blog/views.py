from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View
from .models import BlogPost
from django.urls import reverse_lazy


# Create your views here.


class AllBlogPosts(ListView):
    template_name = 'elements/main/all_posts.html'
    queryset = BlogPost.objects.all()
    context_object_name = 'blog_posts'


class SingleBlogPost(DetailView):
    template_name = 'elements/main/read_post.html'
    model = BlogPost


class CreateBlogPost(CreateView):
    template_name = 'elements/main/new_post.html'
    model = BlogPost
    fields = ['title_text', 'paragraph', 'author_name']
    success_url = reverse_lazy('index')


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
