from django.shortcuts import render
import requests

def cat_fact_view(request):
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()

    context = {
        "fact": data["fact"]
    }

    return render(request, "catfacts/cat_fact.html", context)
