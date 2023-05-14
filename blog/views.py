import json
from os import environ

import requests
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, View, UpdateView

from .models import BlogPost, Cities
from .utils import weatherwidget, datetimeconverter


class AllBlogPosts(ListView):
    template_name = 'all_posts.html'
    model = BlogPost
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        api_key = environ.get('api_key')
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get('city')
        if not city:
            city = 'London'
        check_city = Cities.objects.filter(name=city)
        if not check_city:
            error_message = 'City not found'
            context['error_message'] = error_message
            context['show_modal'] = True
            return context
        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(api_url)
        if response.status_code != 200:
            error_message = f'Error: {response.status_code}'
            context['error_message'] = error_message
            context['show_modal'] = True
            return context
        weather_data = json.loads(response.text)
        sunrise = datetimeconverter.datetimeconverter(weather_data['sys']['sunrise'])
        sunset = datetimeconverter.datetimeconverter(weather_data['sys']['sunset'])
        temperature = weatherwidget.kelvin_to_celsius(weather_data['main']['temp'])
        context['icon'] = weather_data['weather'][0]['icon']
        context['name'] = weather_data['name']
        context['temperature'] = temperature
        context['description'] = weather_data['weather'][0]['description']
        context['country'] = weather_data['sys']['country']
        context['sunrise'] = sunrise
        context['sunset'] = sunset
        return context


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


class ErrorPopupView(View):
    def get(self, request):
        return render(request, template_name='error.html')
