from django.shortcuts import render

# Create your views here.
def Home(request):
	return render(request,'Jobs/home.html')
def About(request):
	return render(request,'Jobs/about.html')
def login(request):
	return render(request,'Jobs/login.html')