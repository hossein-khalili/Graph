from django.shortcuts import render
from django.http import HttpResponse
from vertex.models import Vertex
   
def profile(request, user_id):
	return HttpResponse("You're looking at vertex %s." % user_id)

# Create your views here.
