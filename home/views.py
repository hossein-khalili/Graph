from django.shortcuts import render
from django.http import HttpResponse

def home(requset):
	try:
        usr = request.POST['email']
        pwd = request.POST['password']
    except :
        return HttpResponseRedirect('/')
	return HttpResponse("home.")
# Create your views here.
