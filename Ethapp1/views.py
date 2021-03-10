from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from Ethapp1.Crypto import *

def home(request):
	return render(request, 'log-in/home.html', {})
def EthApp(request):
		if request.method == 'POST':
			address1 = request.POST['address1']
			address2 = request.POST['address2']
			Private_key = request.POST['privatekey'] 
			value = request.POST['value']
			print(Private_key)
			send(address1,address2,Private_key,value)
			messages.success(request, 'You Ether has been sent!')
			return redirect('home')

		else:
			return render(request, 'log-in/index.html', {})
	

# Create your views here.
