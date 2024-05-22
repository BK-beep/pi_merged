from django.contrib import admin
from django.urls import path,include
from blogs.views import *
from CLIENT.views import *
from .views import index



urlpatterns = [
    path('', client_signup, name='signup'),
    path('/admin', admin.site.urls),
    path("/client", include("CLIENT.urls")),
    path("/blog", include("blogs.urls")),
]
