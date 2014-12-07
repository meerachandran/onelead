from django.db import models

# Create your models here.



class Batch(models.Model):
	name=models.CharField(max_length=200)
	start_date=models.DateField('started_date')
	end_date=models.DateField('end_date')
	status=models.CharField(max_length=10)
	currrent_semester=models.CharField(max_length=10)
	
