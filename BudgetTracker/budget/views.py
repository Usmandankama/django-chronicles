from django.shortcuts import render
from .models import Transaction

def transaction_list(request):
    transactions = Transaction.objects.order_by('-date')  # latest first
    return render(request, 'budget/transaction_list.html', {'transactions': transactions})
