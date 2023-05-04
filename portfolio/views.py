from typing import Optional
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Transaction, Account

# Create your views here.
# Function based views

# This function is no longer used due to using the class based view below
def home(request):
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About'})


# Class based views
class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'portfolio/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'transactions'
    ordering = ['-transaction_date']

class TransactionDetailView(DetailView):
    model = Transaction
    context_object_name = 'transaction'

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    context_object_name = 'transaction'
    fields = ['type', 'ticker_symbol', 'price', 'quantity']

    def form_valid(self, form):
        form.instance.account = self.request.user.account #set the account to the current user account
        return super().form_valid(form)
    
class TransactionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transaction
    context_object_name = 'transaction'
    fields = ['type', 'ticker_symbol', 'price', 'quantity']

    def form_valid(self, form):
        form.instance.account = self.request.user.account #set the account to the current user account
        return super().form_valid(form)
    
    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.account.owner:
            return True
        return False
        
class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    context_object_name = 'transaction'
    success_url = '/'
    
    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.account.owner:
            return True
        return False
