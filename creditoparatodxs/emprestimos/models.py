from django.db import models
from django.db.models.fields import related

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    score = models.IntegerField(blank=False, default=0)

class Bank(models.Model):
    name = models.CharField(max_length=60)
    initials = models.CharField(max_length=30)
    score_acceptance = models.IntegerField(blank=False)

class Loan(models.Model):
    borrower = models.ForeignKey("User", on_delete=models.CASCADE, related_name="loans_taken")
    lender = models.ForeignKey("Bank", on_delete=models.CASCADE, related_name="loans_sold")
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=False)
    interest = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    months = models.IntegerField(blank=False, default=0)
    installment = models.DecimalField(max_digits=15, decimal_places=2, blank=False)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)