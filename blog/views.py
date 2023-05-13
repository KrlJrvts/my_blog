from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView
from .models import BlogPost
from django.urls import reverse_lazy


class AllBlogPosts(ListView):
    template_name = 'all_posts.html'
    model = BlogPost
    context_object_name = 'all_posts'


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


class EditBlogPost(UpdateView):
    template_name = 'edit_post.html'
    model = BlogPost
    fields = ['title', 'paragraph', 'author_name']
    success_url = reverse_lazy('all-blog-posts')

    def form_valid(self, form):
        form.instance.author_name = self.request.user
        return super().form_valid(form)


class DeleteBlogPost(View):
    model = BlogPost
    success_url = reverse_lazy('all-blog-posts')

    def get(self, request, post_id):
        post = BlogPost.objects.get(id=post_id)
        post.delete()
        return render(request, 'all_posts.html')


class AboutPage(View):
    template_name = 'about.html'

    def get(self, request):
        all_posts = BlogPost.objects.all()
        context = {'all_posts': all_posts}
        return render(request, context=context, template_name='about.html')
