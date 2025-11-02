from django.shortcuts import render, get_object_or_404

from .models import Person

# Create your views here.

def apppage(request):
    persons = Person.objects.all()
    return render(request, 'index2.html', {'persons': persons})

def person_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, 'person.html', {'person': person})