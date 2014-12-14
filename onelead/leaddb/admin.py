from django.contrib import admin
from leaddb.models import TimeTable
from leaddb.models import Attendance,MentorShip,Batch,Student, Subject, SubjectMap,Staff


admin.site.register(TimeTable)
admin.site.register(Attendance)
admin.site.register(MentorShip)
admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SubjectMap)
admin.site.register(Staff)
