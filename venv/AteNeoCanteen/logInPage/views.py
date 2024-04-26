from django.shortcuts import render

def index(request):
    return render(request, 'logInPage/index.html')

def customer(request):
    return render(request, 'logInPage/customer.html')
