from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
        owner = models.OneToOneField(User, on_delete=models.CASCADE)
        account_name = models.CharField(max_length=100)
        
        date_created = models.DateTimeField(default=timezone.now)
        date_last_modified = models.DateTimeField(auto_now=True)

        def __str__(self):
                return f"{self.owner.username}'s {self.account_name} Portfolio"

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=25)
    transaction_date = models.DateTimeField(default=timezone.now)
    ticker_symbol = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
           return f" Transaction [{self.type}] - {self.ticker_symbol} of {self.quantity} for ${self.price}"