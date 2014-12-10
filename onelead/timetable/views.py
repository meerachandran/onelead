from django.shortcuts import render

from django.template import RequestContext, loader


def time_table(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		template = loader.get_template('batch_form.html')
		context = RequestContext(request)
		print context
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method(may be an ajax call} , so save the data and say "saved"
		#create a Batch object and set variables and save
		return HttpResponse("saved")
