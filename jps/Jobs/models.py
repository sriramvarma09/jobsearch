from django.db import models
from django.utils import timezone
# Create your models here.

class Recuriter(models.Model):
	name=models.CharField(max_length=24)
	password=models.CharField(max_length=24)
	email_address=models.CharField(max_length=60)
	phone=models.CharField(max_length=24)
	companyname=models.CharField(max_length=24)
	created_date=models.DateTimeField(auto_now_add=timezone)
	
	def __str__(self):
		return self.companyname
class User(models.Model):
	name=models.CharField(max_length=24)
	password=models.CharField(max_length=24)
	email_address=models.CharField(max_length=24)
	phone=models.CharField(max_length=24)
	created_date=models.DateTimeField(auto_now_add=timezone)

	def __str__(self):
		return self.name

class Role(models.Model):
	companyname=models.ForeignKey(Recuriter,on_delete=models.CASCADE)
	role=models.CharField(max_length=24)
	def __str__(self):
		return self.role

class Registrations(models.Model):
	status=[("Applied","Applied"),
			("Under Review","Under Review"),
			("Rejected","Rejected"),
			("Selected","Selected")]
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	Jobrole=models.ForeignKey(Role,on_delete=models.CASCADE,blank=True, null=True ,default="")
	Company=models.ForeignKey(Recuriter,on_delete=models.CASCADE)	
	Application_Status=models.CharField(max_length=24,choices=status)

	def __str__(self):
		return self.user.name
