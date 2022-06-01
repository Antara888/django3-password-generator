from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
	return render(request, 'generator/home.html')

def password(request):

	characters = list('abcdefghrjklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&**'))

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	lenght= int(request.GET.get('lenght',12))

	thepassword = ''
	for x in range(lenght):
		thepassword+= random.choice(characters)

	return render(request, 'generator/password.html', {'password':thepassword})

def about(request):

	return render(request, 'generator/about.html')
