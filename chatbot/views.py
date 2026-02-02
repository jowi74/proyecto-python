from django.shortcuts import render
from .forms import ChatbotForm
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chatbot_view(request):
    response_text = None
    form = ChatbotForm()

    if request.method == "POST":
        form = ChatbotForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data["prompt"]

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            response_text = response.text

    return render(request, "chatbot/chatbot.html", {
        "form": form,
        "response": response_text
    })
