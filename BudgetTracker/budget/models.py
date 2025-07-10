from django.db import models

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'Income'),
        ('EX', 'Expense'),
    )
    
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=2, choices=TRANSACTION_TYPES) 
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.title} - {self.amount} ({self.get_type_display()})"