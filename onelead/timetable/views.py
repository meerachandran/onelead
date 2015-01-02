from django.shortcuts import render

from django.template import RequestContext, loader

from django.http import HttpResponse
from leaddb.models import TimeTable
from leaddb.models import SubjectMap
from leaddb.models import  Student
from leaddb.models import Attendance
import json
import datetime
def index(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		maps_list = SubjectMap.objects.all()
		template = loader.get_template('testcal.html')
		context = RequestContext(request,{'maps_list':maps_list})
		print context
		return HttpResponse(template.render(context))
	else:
		#Acessing form using a POST method(may be an ajax call} , so save the data and say "saved"
		#create a Batch object and set variables and save
		return HttpResponse("saved")

def get_slots(request):
	if request.method == 'GET':
		slot_list = TimeTable.objects.all()
		slots=[]
		for slot in slot_list:
			start=slot.start_date_time.strftime("%Y-%m-%d %H:%M:%S")
			end=start=slot.end_date_time.strftime("%Y-%m-%d %H:%M:%S")
			summary=slot.sub_map.mapName()
			slots.append(dict(id=slot.id,summary=summary,startTime=start,
				endTime=end))
		return HttpResponse(json.dumps(slots),content_type = "application/json")
		

from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import ModelForm

class NameForm(ModelForm):
	pass
		



		
def test(request):
	
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'name.html', {'form': form})
