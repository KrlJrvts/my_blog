from django.contrib import admin
from django.urls import path
from blog.views import AllBlogPosts, SingleBlogPost, CreateBlogPost, DeleteBlogPost, AboutPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-post/', CreateBlogPost.as_view(), name='new-post'),
    path('', AllBlogPosts.as_view(), name='all-blog-posts'),
    path('read-post/<int:pk>/', SingleBlogPost.as_view(), name='single-post'),
    path('delete-post/<int:post_id>/', DeleteBlogPost.as_view(), name='delete-post'),
    path('about/', AboutPage.as_view(), name='about-page'),
]
