from openai import OpenAI
from django.conf import settings

def ai_message(user_message):

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.DEEPSEEK_API_KEY,)

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
        { 
        "role": "system",
        "content": "You are a helpful assistant."
        },  
        {
        "role": "user",
        "content": user_message
        }
    ]
    )

    return completion.choices[0].message.content
