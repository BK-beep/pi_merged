from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

urlpatterns = [
    path("", views.client_index , name="client-index"),
    path("signup", views.client_signup , name="client-signup"),
    path("login",views.client_login ,name="client-login"),
    path("logout/", views.client_logout, name="client-logout"),
    path("chat/", views.client_chat , name="client-chat"),
    path("api/send_message/", views.client_send_message , name="client-send-message"),
    path("api/get_message/", views.client_get_message , name="client-get-message"),
    path("api/delete_conversation/<int:pk>", views.client_delete_conversation , name="client-delete"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)