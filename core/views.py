from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SingupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        "categories": categories, 
        "items": items,
        })

def contact(request):
    return render(request, 'core/contact.html')


def singup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SingupForm()
    
    return render(request, 'core/singup.html', {
        'form': form
        })