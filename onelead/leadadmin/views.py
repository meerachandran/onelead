from django.shortcuts import render
from django.template import RequestContext, loader

from django.http import HttpResponse

# Create your views here.

def index(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		template = loader.get_template('main.html')
		context = RequestContext(request)
		print context
		request.session['logined'] = "yes"
		return HttpResponse(template.render(context))
