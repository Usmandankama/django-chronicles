from django.shortcuts import render, redirect
from .models import Transaction, Expense
from django.http import HttpResponse
from .forms import TransactionForm

def transaction_list(request):
    expense = Expense.objects.all()  # Fetch all expenses
    transactions = Transaction.objects.order_by('-date')  # latest first
    return render(request, 'budget/transaction_list.html', {'transactions': transactions, 'expense': expense})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction-list')
        # ❌ Don't reset the form here — just let it fall through and render with errors
    else:
        form = TransactionForm()

    return render(request, 'budget/add_transaction.html', {'form': form})


def add_expense(request):
    return HttpResponse("Form page coming soon!")

