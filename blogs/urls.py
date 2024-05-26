from django.contrib import admin
from django.urls import path,include
from blogs.views import *



urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('blogPosts', blog_posts, name='blog_posts'),
    path('add-post', add_post, name='add_post'),
    path('profile', profile, name='profile'),
    path('comments/', comments, name='comments'),
    path('post/<int:blog_id>/', blog_details, name="blog_details"),
    path('category/<category>/', blog_category, name='blog_category'),
    path('__reload__/', include('django_browser_reload.urls')),
    path('add-comment/<slug:slug>/', add_comment, name='add_comment'),
    path('reply/<int:comment_id>/', reply, name='reply'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send/', send_newsletter, name='send_newsletter'),
    path('thank_you/', thank_you, name='thank_you'),
    path('newsletter_sent/', newsletter_sent, name='newsletter_sent'),
]
