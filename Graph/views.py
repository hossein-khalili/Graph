from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect

def firstpage(request):
	try:
		eml = request.COOKIES['email']
		pwd = request.COOKIES['password']
	except :
		print firstpage
		return render_to_response('firstpage.html',{},context_instance=RequestContext(request))
	print 'Graph/Graph/views.py: usr:',eml,'  pwd: ',pwd
	return HttpResponseRedirect('/home/')

# Create your views here.
