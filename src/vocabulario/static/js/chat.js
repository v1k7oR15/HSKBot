document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('chat-form');
    const input = form.querySelector('input[name="mensaje"]');
    const button = form.querySelector('button[type="submit"]');
    const chatMessages = document.getElementById('chat-Messages');
    const noMessages = document.getElementById('no-messages');

    form.addEventListener('submit', async function (e) {
        // Si no hay mensajes, ocultar el mensaje de "No hay mensajes"
        if (noMessages) {
            noMessages.style.display = 'none';
        }

        e.preventDefault();

        const mensaje = input.value.trim();
        if (!mensaje) return;

        // Mostrar el mensaje del usuario inmediatamente
        const userPhotoUrl = window.userPhotoUrl || "/static/img/profilepicture.png";
        const userMessageDiv = document.createElement('div');
        userMessageDiv.className = "flex w-full mt-2 space-x-3 max-w-xl ml-auto justify-end";
        userMessageDiv.innerHTML = `
            <div>
                <div class="bg-blue-600 p-3 rounded-lg">
                    <p class="text-sm text-white">${mensaje.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</p>
                </div>
            </div>
            <div class="flex-shrink-0 h-10 w-10 rounded-full overflow-hidden">
                <img src="${userPhotoUrl}" alt="Avatar usuario" class="h-full w-full object-cover" />
            </div>
        `;
        chatMessages.appendChild(userMessageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // Limpiar input y bloquear
        input.value = '';
        input.disabled = true;
        button.disabled = true;

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        try {
            const response = await fetch(window.location.href, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ mensaje }),
            });

            if (response.ok) {
                const data = await response.json();
                chatMessages.innerHTML = data.html;
                chatMessages.scrollTop = chatMessages.scrollHeight;
            } else {
                alert('Error enviando el mensaje');
            }
        } catch (error) {
            alert('Error de red');
        } finally {
            input.disabled = false;
            button.disabled = false;
            input.focus();
        }
    });
});