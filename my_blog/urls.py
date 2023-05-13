from django.contrib import admin
from django.urls import path
from blog.views import AllBlogPosts, CreateBlogPost, DeleteBlogPost, AboutPage, get_single_post, EditBlogPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-post/', CreateBlogPost.as_view(), name='new-post'),
    path('', AllBlogPosts.as_view(), name='all-blog-posts'),
    path('read-post/<int:post_id>/', get_single_post, name='single-post'),
    path('delete-post/<int:post_id>/', DeleteBlogPost.as_view(), name='delete-post'),
    path('about/', AboutPage.as_view(), name='about-page'),
    path('edit-post/<int:pk>/', EditBlogPost.as_view(), name='edit-post'),

]
