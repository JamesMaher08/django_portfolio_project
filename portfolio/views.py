from django.shortcuts import render
from .models import Transaction, Account



# Create your views here.
def home(request):
    context = {
        'transactions': Transaction.objects.all()
    }

    return render(request, 'portfolio/home.html', context)

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About'})
