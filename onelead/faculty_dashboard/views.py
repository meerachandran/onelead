from django.shortcuts import render


from django.template import RequestContext, loader

from django.http import HttpResponse
from leaddb.models import SubjectMap
import json

from leaddb.models import Student

def batch_list(request):
	if request.method == 'GET':
		#Acessing form using a GET method , so deliver a form
		maps_list = SubjectMap.objects.filter(staff__id='1')
		template = loader.get_template('batch_list.html')
		context = RequestContext(request,{'maps_list':maps_list})
		print context
		return HttpResponse(template.render(context))

def student_list(request,batchid):

	studentsObjs=Student.objects.filter(batch__id=batchid)

	students=[]
	for student in studentsObjs:
		students.append(dict(id=student.id,name=student.name))
	return HttpResponse(json.dumps(students),content_type = "application/json")

def batch_maps(request,staffid):
	mapObjs=SubjectMap.objects.filter(staff__id=staffid)

	batchMaps=[]
	for _map in mapObjs:
		batchMaps.append(dict(id=_map.id,batch_name=_map.batch.name,sub_name=_map.subject.name))
	return HttpResponse(json.dumps(	batchMaps),content_type = "application/json")
