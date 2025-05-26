from django.urls import path
from .views import base_view, chat_view

urlpatterns = [
    path('', base_view, name='inicio'),
    path('chat/', chat_view, name='chat'),
]