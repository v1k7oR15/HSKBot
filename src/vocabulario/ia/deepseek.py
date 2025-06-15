from openai import OpenAI
from django.conf import settings

def ai_message(user_message, messages):
    client = OpenAI(api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

    full_messages = [{"role": "system", "content": settings.PROMPT}]
    full_messages.extend(messages)
    full_messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=full_messages,
        stream=False
    )

    return response.choices[0].message.content