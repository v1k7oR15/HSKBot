document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('chat-form');
    const input = form.querySelector('input[name="mensaje"]');
    const button = form.querySelector('button[type="submit"]');
    const chatMessages = document.getElementById('chat-Messages');


    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const noMessages = document.getElementById('no-messages');
        noMessages.remove();

        // Deshabilita el input y el botón
        input.disabled = true;
        button.disabled = true;

        // Añade el mensaje del usuario al chat inmediatamente
        const userMsgDiv = document.createElement('div');
        userMsgDiv.className = "flex w-full mt-2 space-x-3 max-w-xs ml-auto justify-end";
        userMsgDiv.innerHTML = `
            <div>
                <div class="bg-blue-600 p-3 rounded-lg">
                    <p class="text-sm text-white">${input.value}</p>
                </div>
            </div>
            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300"></div>
        `;
        chatMessages.appendChild(userMsgDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // 2. Guarda el mensaje y limpia el input
        const mensaje = input.value;
        input.value = '';

        // 3. Envía el mensaje por AJAX
        fetch(window.location.pathname, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({ 'mensaje': mensaje })
        })
            .then(response => response.json())
            .then(data => {
                chatMessages.innerHTML = data.html;
                chatMessages.scrollTop = chatMessages.scrollHeight;
                // Habilita el input y el botón
                input.disabled = false;
                button.disabled = false;
                input.focus();
            });
    });
});
