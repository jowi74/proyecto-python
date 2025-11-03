from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Person, Product
from .forms import UploadProduct


def apppage(request):
    persons = Person.objects.all()
    return render(request, 'index2.html', {'persons': persons})


def person_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, 'person.html', {'person': person})

@login_required(login_url="/users/login/")
def product_list_view(request):
    
    product_list = Product.objects.all()[:20]

    if request.method == 'POST':
        form = UploadProduct(request.POST)
        if form.is_valid():
            newproduct = form.save(commit=False)
            newproduct.user = request.user  # asigna usuario
            newproduct.save()
            return redirect('products_list')  # redirecciona
    else:
        form = UploadProduct()

    return render(request, 'products/list.html', {
        'product_list': product_list,
        'form': form
    })
