from django.shortcuts import render

def login(request):
	return render_to_response('firstpage.html', context_instance=RequestContext(request))

def logout(request):
	return render_to_response('firstpage.html', context_instance=RequestContext(request))
    
# Create your views here.
