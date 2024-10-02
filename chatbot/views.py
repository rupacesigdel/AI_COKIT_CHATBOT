from django.shortcuts import render
from .models import Chat
import copilotkit

def chat_view(request):
    try:
        copilot = copilotkit.CopilotKitState(api_key='ck_pub_a001bbe9ba7329b1e8f207a9d9ca0f1a')
    except AttributeError as e:
        return render(request, 'chatbot/chat.html', {'error': 'CopilotKit Client is not available.'})

    if request.method == 'POST':
        user_message = request.POST.get('message')

        try:
            print(f"User message: {user_message}")
            bot_response = copilot
            if isinstance(bot_response, dict):
                bot_response = bot_response.get('response', 'No response found')

        except Exception as e:
            return render(request, 'chatbot/chat.html', {'error': 'Error generating chat response.'})

        chat = Chat.objects.create(user_message=user_message, bot_response=bot_response)
        chat.save()

        chats = Chat.objects.all().order_by('-timestamp')
        return render(request, 'chatbot/chat.html', {'chats': chats})

    chats = Chat.objects.all().order_by('-timestamp')
    return render(request, 'chatbot/chat.html', {'chats': chats})
