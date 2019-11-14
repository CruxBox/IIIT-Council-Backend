from django.db import models
from django.contrib.auth.models import PermissionsMixin
from colleges.models import College

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','first_name','last_name','phone_no']
    
    #attributes
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    phone_no = models.CharField(max_length=13,null=False)

    def __str__(self):
    	return first_name + ' ' + last_name

class Admin(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	college = models.ForeignKey(College, on_delete = models.CASCADE)

class Professors(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	visitingFaculty = models.BooleanField( default = false)
	
	#faculty can be visiting faculty to other institutes. Also, an institute may have many professors
	colleges = models.ManyToManyField('College')

	#add more fields accordingly
	DEPARTMENT_CHOICES = (
		(COMPUTER_SCIENCE, "CSE"),
		(ELECTRONICS, "ECE")
		)
	department = CharField(
		max_length=10, 
		choices = DEPARTMENT_CHOICES,
		default=None
		)

	class Meta:
		permissions = [
			("view_Professor", "Can view professor"), 
			("add_Professor", "Can add professor"), 
			("change_Professor", "Can change professor"), 
			("delete_Professor", "Can delete professor"), 
            ]
	#Research Areas?
	#Add fields accordingly

class Directors(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mentor = models.BooleanField( default = false)
	
	college = models.ForeignKey(College, on_delete = modesls.CASCADE)
	
	"""
	
	if a professor, add one to one field with director
	is_professor = models.BooleanField( default = false )
	professor = models.ForeignKey(Professor, on_delete = models.SET_NULL)
	
	"""

	class Meta:
		permissions = [
			("view_Director", "Can view director"), 
			("add_Director", "Can add director"), 
			("change_Director", "Can change director"), 
			("delete_Director", "Can delete director"), 
			]
	#Add fields accordingly

class Staff(models.Model):
	user = models.OnetotOneField(User,on_delete = models.CASCADE)

	#ManagementPerson will be specific to one institute.
	college = models.ForeignKey(College, on_delete = models.CASCADE)

	#position choices and position attribute

	DEPARTMENT_CHOICES = (
		(FINANCE, "Finance"),
		(ACADEMICS, "Academics")
		)
	department = CharField(
		max_length=20,
		choices = DEPARTMENT_CHOICES,
		default = None
		)
	class Meta:
		permissions = [
			("view_Staff", "Can view staff"), 
			("add_Staff", "Can add staff"), 
			("change_Staff", "Can change staff"), 
			("delete_Staff", "Can delete staff"), 
    		]
	#Add fields accordingly