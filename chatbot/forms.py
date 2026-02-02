from django import forms

class ChatbotForm(forms.Form):
    prompt = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "flex-1 p-2 border rounded-lg",
                "placeholder": "Escribe un mensaje..."
            }
        )
    )
