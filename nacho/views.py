from django.shortcuts import render
from nacho2.models import Person

def homepage(request):
    person_list = Person.objects.all()
    return render(request, 'index.html',{'persons': person_list })