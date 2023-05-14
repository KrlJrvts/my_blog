from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, View, UpdateView

from .models import BlogPost, Cities
import requests
import json
from .utils.weatherwidget import kelvin_to_celsius


class AllBlogPosts(ListView):
    template_name = 'all_posts.html'
    model = BlogPost
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):

        city = self.request.GET.get('city')
        check_city = Cities.objects.filter(name=city)
        if not check_city:
            city = 'London'

        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5847d008c20b2a95956c42f581f481c6'

        response = requests.get(api_url)

        """ add error handling"""
        if response.status_code != 200:
            return HttpResponse(f'Error: {response.status_code}')

        weather_data = json.loads(response.text)
        temperature = kelvin_to_celsius(weather_data['main']['temp'])
        context = {
            'icon': weather_data['weather'][0]['icon'],
            'name': weather_data['name'],
            'temperature': temperature,
            'description': weather_data['weather'][0]['description']
        }
        return super().get_context_data(**context, **kwargs)


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

    def get(self, request, post_id):
        post = BlogPost.objects.get(id=post_id)
        post.delete()
        success_url = reverse('all-blog-posts')
        return redirect(success_url)


class AboutPage(View):

    def get(self, request):
        all_posts = BlogPost.objects.all()
        context = {'all_posts': all_posts}
        return render(request, context=context, template_name='about.html')

