from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def index(request):
    return render(request, 'main/index.html')

def about(request):
    error =''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('about')
        else:
            error = "Неправильно заполнено"

    form = ContactForm()
    date = {
        'form': form,
        'error': error
    }

    return render(request, 'main/about.html', date)

