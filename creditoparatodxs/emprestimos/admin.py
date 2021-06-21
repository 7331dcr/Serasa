from django.contrib import admin
from .models import Bank, Loan, User

# Register your models here.
admin.site.register(Bank)
admin.site.register(Loan)
admin.site.register(User)