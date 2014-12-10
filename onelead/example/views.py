from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.


from django.http import HttpResponse
from leaddb.models import Batch


#This one is for dojo based ajax request demo
def batch_form(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		template = loader.get_template('batch_form.html')
		context = RequestContext(request)
		print context
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method(may be an ajax call} , so save the data and say "saved"
		#create a Batch object and set variables and save
		batch=Batch()
		batch.name=request.POST['name']
		batch.start_date=request.POST['startdate']
		batch.end_date=request.POST['enddate']
		batch.status='Live'
		batch.semester='1'
		batch.save()
		
		#retrieve all saved data and send bak to dojo
		dbdata=""
		batches=Batch.objects.all() #Retrieve all batches from db
		for batch in batches:
			dbdata=dbdata+" "+batch.name
		print dbdata
		return HttpResponse("saved"+dbdata)

#Simple form without dojo
#difference is only in the template
def batch_form_simple(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		template = loader.get_template('batch_form_simple.html')
		context = RequestContext(request)
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method, so save the data and say "saved"
		print request.POST['name']
		#create a Batch object and set variables and save
		batch=Batch()
		batch.name=request.POST['name']
		batch.start_date=request.POST['startdate']
		batch.end_date=request.POST['enddate']
		batch.status='Live'
		batch.semester='1'
		batch.save()
		
		#retrieve all saved data and send bak to dojo
		
		return HttpResponse(request.session['logined'])



#URL to print db vales to browser
def print_db(request):
	dbdata=""
	batches=Batch.objects.all() #Retrieve all batches from db
	for batch in batches:
		dbdata=dbdata+" "+batch.name
	print dbdata
		#say "saved" back to dojo
	return HttpResponse(dbdata)
	
	
