from django.shortcuts import render

from django.http import HttpResponse



def index(request):
    latest_question_list = []
    context = {'latest_question_list': latest_question_list}
    return render(request, 'att.html', context)

def get_slots(request):
		latest_question_list = ['hello']
		context = {'latest_question_list': latest_question_list}
		return render(request, 'att.html', context)

def add_students(request):
		latest_question = ['hello']
		context = {'latest_question': latest_question}
		return render(request, 'add.html', context)


#Save add student form url
def submit_students(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		template = loader.get_template('submit.html')
		context = RequestContext(request)
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method, so save the data and say "saved"
		print request.POST['sname']
		#create a Batch object and set variables and save
		Student=Student()
		Student.name=request.POST['sname']
		Student.batch=request.POST['batch']
		Student.gender=request.POST['sgender']
		Student.address=request.POST['address']
		Student.emergency_phone_no=request.POST['ephno']
		Student.mobile_no=request.POST['mno']
		Student.email=request.POST['semail']
		Student.parents=request.POST['parents']
		Student.education_history=request.POST['ehistory']
		Student.admitted_date=request.POST['admndate']
		Student.save()
		
		#retrieve all saved data and send bak to dojo
		dbdata=""
		students=Student.objects.all() #Retrieve all batches from db
		for satch in students:
			dbdata=dbdata+" "+Student.name
		print dbdata
		#Instead of this render the form again
		return HttpResponse("Saved one, so total :"+dbdata)
