from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View
from .models import BlogPost
from django.urls import reverse_lazy


class AllBlogPosts(ListView):
    template_name = 'all_posts.html'
    model = BlogPost


def get_all_posts(request):
    all_posts = BlogPost.objects.all()
    return render(
        request,
        'all_posts.html',
        {
            'all_posts': all_posts,
            'title': 'All Posts',
        }
    )


class Navigation(ListView):
    template_name = 'all_posts.html'
    model = BlogPost


def get_single_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    all_posts = BlogPost.objects.all()
    return render(
        request,
        'single_post.html',
        {
            'post': post,
            'all_posts': all_posts,
            'title': 'Single Post',
        }
    )


class CreateBlogPost(CreateView):
    template_name = 'create_post.html'
    model = BlogPost
    fields = ['title', 'paragraph', 'author_name']
    success_url = reverse_lazy('all-blog-posts')

    def form_valid(self, form):
        form.instance.author_name = self.request.user
        return super().form_valid(form)


class DeleteBlogPost(View):
    def get(self, request, post_id):
        post = BlogPost.objects.get(id=post_id)
        post.delete()
        return render(request, 'all_posts.html')


class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')
