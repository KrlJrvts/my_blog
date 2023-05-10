"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import AllBlogPosts, SingleBlogPost, CreateBlogPost, DeleteBlogPost, AboutPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-post', CreateBlogPost.as_view(), name='new-post'),
    path('', AllBlogPosts.as_view(), name='all-blog-posts'),
    path('read-post/<int:pk>/', SingleBlogPost.as_view(), name='single-post'),
    path('delete-post/<int:post_id>/', DeleteBlogPost.as_view(), name='delete-post'),
    path('about/', AboutPage.as_view(), name='about-page'),

]
