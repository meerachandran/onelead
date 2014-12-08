from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.


from django.http import HttpResponse
from leaddb.models import Staff


#This one is for dojo based ajax request demo
def add_faculty(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		template = loader.get_template('add_faculty.html')
		context = RequestContext(request)
		print context
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method(may be an ajax call} , so save the data and say "saved"
		print request.POST['name']
		#create a Batch object and set variables and save
		staff=Staff()
		staff.emp_no=request.POST['empno']
		staff.name=request.POST['name']
		staff.gender=request.POST['gender']
		staff.address=request.POST['address']
		staff.emergency_phone_no=request.POST['ephno']
		staff.mobile_no=request.POST['mno']
		staff.email=request.POST['email']
		staff.education_history=request.POST['ehistory']
		staff.joined_date=request.POST['jdate']
		staff.emp_type=request.POST['emptype']
		staff.save()
		
		#retrieve all saved data and send bak to dojo
		dbdata=""
		staffs=Staff.objects.all() #Retrieve all batches from db
		for staff in staffs:
			dbdata=dbdata+" "+staff.name
		print dbdata
		return HttpResponse("Saved one, so total :"+dbdata)


