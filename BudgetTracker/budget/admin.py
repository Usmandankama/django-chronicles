from django.contrib import admin
from .models import Transaction
from .models import Expense

# Register your models here.

admin.site.register(Transaction)
admin.site.register(Expense)