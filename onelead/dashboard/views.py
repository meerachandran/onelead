from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.


from django.http import HttpResponse




#This one is for dojo based ajax request demo
def index(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		context = RequestContext(request)
		template = loader.get_template('add_dashboard.html')
		print context
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method(may be an ajax call} , so save the data and say "saved"
		#create a Batch object and set variables and save
		
		return HttpResponse("Saved one")

		

