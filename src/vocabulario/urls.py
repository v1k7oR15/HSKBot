from django.urls import path
from .views import base_view, chat_view, login_view, register_view

urlpatterns = [
    path('', base_view, name='inicio'),
    path('chat/', chat_view, name='chat'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]