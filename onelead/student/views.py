from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.


from django.http import HttpResponse
from leaddb.models import Student
from leaddb.models import Batch


#This one is for dojo based ajax request demo
def add_student(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		batch_list = Batch.objects.all()
		template = loader.get_template('add_student.html')
		context = RequestContext(request,{'batch_list': batch_list})
		print context
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method(may be an ajax call} , so save the data and say "saved"
		print request.POST['name']
		#create a Student object and set variables and save
		student=Student()
		student.admission_no=request.POST['adno']
		batch_id=request.POST['selbatch']
		print "mahesh",batch_id
		student.batch=Batch.objects.filter(id=batch_id)[0]
		student.name=request.POST['name']
		student.gender=request.POST['gender']
		student.address=request.POST['address']
		student.emergency_phone_no=request.POST['ephno']
		student.mobile_no=request.POST['mno']
		student.email=request.POST['email']
		student.parents=request.POST['parents']
		student.education_history=request.POST['edu_history']
		student.admitted_date=request.POST['ad_date']
		student.save()
		
		#retrieve all saved data and send bak to dojo
		dbdata=""
		students=Student.objects.all() #Retrieve all Studentes from db
		for student in students:
			dbdata=dbdata+" "+student.name
		print dbdata
		return HttpResponse("Saved one, so total :"+dbdata)

#Get batch names from batch table.

