from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.


from django.http import HttpResponse
from leaddb.models import Attendance
from leaddb.models import Student


def index(request):
    latest_question_list = []
    context = {'latest_question_list': latest_question_list}
    return render(request, 'att.html', context)


#Add attendance based on dojo ajax.
def add_attendance(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		student_list = Student.objects.all()
		template = loader.get_template('add_attendance.html')
		context = RequestContext(request,{'student_list': student_list})
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method(may be an ajax call} , so save the data and say "saved"
		print request.POST
		#create a Batch object and set variables and save
		attendance=Attendance()
		attendance.time_slt=request.POST['empno']
		attendance.student=Student.objects.filter(id=student_id)
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



