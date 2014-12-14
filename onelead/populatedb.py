import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onelead.settings")
import random
from leaddb.models import *
import django
django.setup()

Batch.objects.all().delete()
for i in range(0,10):
	batch=Batch()
	batch.name='MBA2014-16-test'+str(random.randint(1,100))
	batch.start_date='2014-10-10'
	batch.end_date='2016-10-10'
	batch.status='Live'
	batch.currrent_semester='1'
	batch.save()

Student.objects.all().delete()

a_live_batch=Batch.objects.filter(status='Live')[0]

for i in range(0,70):
	stud=Student()
	stud.admission_no='L12'+str(random.randint(1,100))
	stud.batch = a_live_batch
	stud.name='mahesh-test'+str(random.randint(1,100))
	stud.gender='M'
	stud.address='Leelanivas,muttathiparampu PO, Cherthala'
	stud.emergency_phone_no='9995286241'
	stud.mobile_no='9995286241'
	stud.email='mahesh@lead.com'
	stud.parents='P chandarsekharan Nair, Leela'
	stud.education_history='Mtech'
	stud.admitted_date='2014-10-10'
	stud.save()

Staff.objects.all().delete()
for i in range(0,5):
	staff=Staff()
	staff.emp_no='LE12'+str(random.randint(1,100))	
	staff.name='Meera-test'+str(random.randint(1,100))
	staff.gender='F'
	staff.address='Leelanivas,muttathiparampu PO, Cherthala'
	staff.emergency_phone_no='9995286241'
	staff.mobile_no='9995286241'
	staff.email='mahesh@lead.com'
	staff.parents='P chandarsekharan Nair, Leela'
	staff.education_history='Mtech'
	staff.joined_date='2014-10-10'
	staff.emp_type='Teaching'
	staff.save()
	
	
a_staff=Staff.objects.filter(gender='F')[0]

Subject.objects.all().delete()
for i in range(0,10):
	sub=Subject()
	sub.name='History 101-'+str(random.randint(1,100))
	sub.save()
a_subject=Subject.objects.all()[0]
	
	
SubjectMap.objects.all().delete()
for i in range(0,1):
	sub=SubjectMap()
	sub.subject=a_subject
	sub.staff=a_staff
	sub.batch=a_live_batch
	sub.save()

a_subject_map=SubjectMap.objects.all()[0]

EventTypes.objects.all().delete()
types=['Lecture','Festival', 'Seminar' , 'project']
for i in range(0,3):
	etype=EventTypes()
	etype.name=types[i]
	etype.save()

TimeTable.objects.all().delete()
an_event=EventTypes.objects.all()[0]
a_subject=Subject.objects.all()[0]
for i in range(0,10):
	tt=TimeTable()
	tt.sub_map=a_subject_map
	tt.start_date_time='2014-12-'+str(random.randint(1,25))+' 08:00:00'
	tt.end_date_time='2014-12-'+str(random.randint(1,25))+' 10:00:00'
	tt.save()
for i in range(0,3):
	tt=TimeTable()
	tt.sub_map=a_subject_map
	tt.start_date_time='2014-12-10 08:00:'+str(random.randint(10,22))
	tt.end_date_time='2014-12-10 08:00:23'
	tt.save()

Attendance.objects.all().delete()

	





