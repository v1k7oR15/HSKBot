from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from .ia.deepseek import ai_message
from .forms import RegistroForm, LoginForm
from django.contrib.auth.models import User

def base_view(request):
    # Recupera el historial de la sesión o crea uno nuevo
    return render(request, 'inicio.html')

def chat_view(request):
    # Esta vista es para manejar la lógica del chat
    mensajes = request.session.get('mensajes', [])

    if request.method == 'POST':
        user_message = request.POST.get('mensaje')
        if user_message:
            # Añade primero el mensaje del usuario
            mensajes.append({"role": "user", "content": user_message})
            # Luego la respuesta de la IA
            respuesta = ai_message(user_message)
            mensajes.append({"role": "assistant", "content": respuesta})
        request.session['mensajes'] = mensajes

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('chat_messages.html', {'mensajes': mensajes}, request=request)
        return JsonResponse({'html': html})
    return render(request, 'chat.html', {'mensajes': mensajes})

def login_view(request):
    form = LoginForm(request.POST or None)
    error = None
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember_me = request.POST.get('remember_me')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)
                    if remember_me:
                        # 30 días (en segundos)
                        request.session.set_expiry(60 * 60 * 24 * 30)
                    else:
                        # Sesión expira al cerrar el navegador
                        request.session.set_expiry(0)
                    return redirect('inicio')
                else:
                    error = "Correo o contraseña incorrectos"
            except User.DoesNotExist:
                error = "Correo o contraseña incorrectos"
    return render(request, 'login.html', {'form': form, 'error': error})

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})