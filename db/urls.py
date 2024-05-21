"""
URL configuration for db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from blogs.views import *
from .views import index



urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('admin/', admin.site.urls),
    path('', blog_posts, name='blog_posts'),
    path('blog/blogPosts', blog_posts, name='blog_posts'),
    path('profile', profile, name='profile'),
    path('comments/', comments, name='comments'),
    path("post/<int:blog_id>/", blog_details, name="blog_details"),
    path("category/<category>/", blog_category, name="blog_category"),
    path("__reload__/", include("django_browser_reload.urls")),
    path('add-comment/<slug:slug>/', add_comment, name='add_comment'),
    path('reply/<int:comment_id>/', reply, name='reply'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send/', send_newsletter, name='send_newsletter'),
    path('thank_you/', thank_you, name='thank_you'),
    path('newsletter_sent/', newsletter_sent, name='newsletter_sent'),
]
