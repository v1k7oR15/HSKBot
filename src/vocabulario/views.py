from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .ia.deepseek import ai_message

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