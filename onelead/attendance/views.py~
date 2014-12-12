from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.


from django.http import HttpResponse
from leaddb.models import Attendance
from leaddb.models import Student
from leaddb.models import TimeTable


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
		#attendance.time_table_slot=TimeTable.objects.filter(id=timetable_id)
		#attendance.student=Student.objects.filter(id=student_id)
		attendance.save()
		#retrieve all saved data and send bak to dojo
		dbdata=""
		staffs=Staff.objects.all() #Retrieve all batches from db
		for staff in staffs:
			dbdata=dbdata+" "+staff.name
		print dbdata
		return HttpResponse("Saved one, so total :"+dbdata)
json="""[
	{ "abbreviation": "AL", "name": "Alabama" },
	{ "abbreviation": "AK", "name": "Alaska" },
	{ "abbreviation": "AZ", "name": "Arizona" },
	{ "abbreviation": "AR", "name": "Arkansas" },
	{ "abbreviation": "CA", "name": "California" },
	{ "abbreviation": "CO", "name": "Colorado" },
	{ "abbreviation": "CT", "name": "Connecticut" },
	{ "abbreviation": "DE", "name": "Delaware" },
	{ "abbreviation": "FL", "name": "Florida" },
	{ "abbreviation": "GA", "name": "Georgia" },
	{ "abbreviation": "HI", "name": "Hawaii" },
	{ "abbreviation": "ID", "name": "Idaho" },
	{ "abbreviation": "IL", "name": "Illinois" },
	{ "abbreviation": "IN", "name": "Indiana" },
	{ "abbreviation": "IA", "name": "Iowa" },
	{ "abbreviation": "KS", "name": "Kansas" },
	{ "abbreviation": "KY", "name": "Kentucky" },
	{ "abbreviation": "LA", "name": "Louisiana" },
	{ "abbreviation": "ME", "name": "Maine" },
	{ "abbreviation": "MD", "name": "Maryland" },
	{ "abbreviation": "MA", "name": "Massachusetts" },
	{ "abbreviation": "MI", "name": "Michigan" },
	{ "abbreviation": "MN", "name": "Minnesota" },
	{ "abbreviation": "MS", "name": "Mississippi" },
	{ "abbreviation": "MO", "name": "Missouri" },
	{ "abbreviation": "MT", "name": "Montana" },
	{ "abbreviation": "NE", "name": "Nebraska" },
	{ "abbreviation": "NV", "name": "Nevada" },
	{ "abbreviation": "NH", "name": "New Hampshire" },
	{ "abbreviation": "NJ", "name": "New Jersey" },
	{ "abbreviation": "NM", "name": "New Mexico" },
	{ "abbreviation": "NY", "name": "New York" },
	{ "abbreviation": "NC", "name": "North Carolina" },
	{ "abbreviation": "ND", "name": "North Dakota" },
	{ "abbreviation": "OH", "name": "Ohio" },
	{ "abbreviation": "OK", "name": "Oklahoma" },
	{ "abbreviation": "OR", "name": "Oregon" },
	{ "abbreviation": "PA", "name": "Pennsylvania" },
	{ "abbreviation": "RI", "name": "Rhode Island" },
	{ "abbreviation": "SC", "name": "South Carolina" },
	{ "abbreviation": "SD", "name": "South Dakota" },
	{ "abbreviation": "TN", "name": "Tennessee" },
	{ "abbreviation": "TX", "name": "Texas" },
	{ "abbreviation": "UT", "name": "Utah" },
	{ "abbreviation": "VT", "name": "Vermont" },
	{ "abbreviation": "VA", "name": "Virginia" },
	{ "abbreviation": "WA", "name": "Washington" },
	{ "abbreviation": "WV", "name": "West Virginia" },
	{ "abbreviation": "WI", "name": "Wisconsin" },
	{ "abbreviation": "WY", "name": "Wyoming" }
]"""
import json
from datetime import datetime
def get_slots(request):
	if request.method == 'GET':
		date=datetime.strptime(request.GET['date'] , '%m/%d/%Y').date()
		date_str=date.strftime('%Y-%m-%d')
		slot_list = TimeTable.objects.filter(start_date_time=date_str)
		slots=[]
		for slot in slot_list:
			slots.append(dict(id=slot.id,summary=slot.summary))
		return HttpResponse(json.dumps(slots),content_type = "application/json")
		



