from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class paymentParty(models.Model):
	Name = models.CharField(max_length = 100)
	Service = models.CharField(max_length = 100, default ='Electricy')
	Num = models.IntegerField()
	def __str__(self):
		return "Inwi internet service"
class Bill(models.Model):
	price = models.IntegerField()
	bill_date = models.DateField()
	paiment_due = models.DateField()
	bill_Provider = models.ForeignKey(paymentParty, on_delete = models.CASCADE)
	client = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return "New Bill From {}, Cost:{}DH".format(self.bill_Provider,self.price)



