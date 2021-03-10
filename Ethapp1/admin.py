from django.contrib import admin
from .models import Bill, paymentParty
# Register your models here.
admin.site.register(Bill)
admin.site.register(paymentParty)