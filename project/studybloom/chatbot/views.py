# views.py
import openai
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage  # If you're saving chat history
from django.views.decorators.csrf import csrf_exempt

# Your OpenAI API key
openai.api_key = 'your-api-key'


@csrf_exempt  # Disable CSRF for simplicity in this example
def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')

        # Generate response from OpenAI GPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )

        bot_message = response['choices'][0]['text'].strip()

        # Optionally save chat history
        ChatMessage.objects.create(user_message=user_message, bot_response=bot_message)

        return JsonResponse({'response': bot_message})

    return render(request, 'chatbot/chat.html')

from django.http import JsonResponse

# Function to handle chat requests
def chat_view(request):
    # Get the user's message from the query parameters
    user_message = request.GET.get('message', '')

    # Process the message (you can modify this logic to make it more advanced)
    response_message = "This is the bot's response."

    # Return the response as JSON
    return JsonResponse({"response": response_message})
