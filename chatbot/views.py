from django.shortcuts import render
from .models import Chat
import copilotkit

def chat_view(request):
    try:
        copilot = copilotkit.Client(api_key='API')
    except AttributeError as e:
        print(f"Error: {e}")
        return render(request, 'chatbot/chat.html', {'error': 'CopilotKit Client is not available.'})
    
    if request.method == 'POST':
        user_message = request.POST.get('message')

        bot_response = copilot.chat(user_message)

        chat = Chat.objects.create(user_message=user_message, bot_response=bot_response)
        chat.save()
        
        chats = Chat.objects.all().order_by('-timestamp')
        return render(request, 'chatbot/chat.html', {'chats': chats})
    
    chats = Chat.objects.all().order_by('-timestamp')
    return render(request, 'chatbot/chat.html', {'chats': chats})
