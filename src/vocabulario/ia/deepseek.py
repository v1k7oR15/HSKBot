from openai import OpenAI
from django.conf import settings

def ai_message(user_message):

    client = OpenAI(api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": settings.PROMPT},
            {"role": "user", "content": user_message},
        ],
        stream=False
    )

    return response.choices[0].message.content