from django.urls import path
from .views import base_view, chat_view, login_view, register_view, palabra_view, mostrar_palabras_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', base_view, name='inicio'),
    path('chat/', chat_view, name='chat'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('palabra/', palabra_view, name='palabra'),
    path('mostrar_palabras', mostrar_palabras_view, name='mostrar_palabras'),
]
