from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from colleges.models import College


class UserManager(BaseUserManager):
	def create_user(self, email, password, is_active = True, is_superuser = False, is_admin  = False, is_staff = False):
		if not email:
			return ValueError('You need to provide an email.')
		user = self.model(email = self.normalize_email(email))

		user.set_password(password)
		user.active = is_active
		user.superuser = is_superuser
		user.admin = is_admin
		user.staff = is_staff

		return user

	def create_superuser(self, email, password):
		user = self.create_user(
			email, 
			password,
			is_active=True,
			is_superuser=True,
			is_admin=True, 
			is_staff=True
			)

		return user
	def create_admin(self, email, password):
		user = self.create_user(
			email, 
			password,
			is_active=True,
			is_superuser=False,
			is_admin=True, 
			is_staff=True
			)

		return user
	def create_staff(self, email, password):
		user = self.create_user(
			email, 
			password,
			is_active=True,
			is_superuser=False,
			is_admin=False, 
			is_staff=True
			)

		return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','first_name','last_name','phone_no']

    #different permissions
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False) 
    superuser = models.BooleanField(default = False)

    #attributes
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50,null=True)
    email= models.EmailField(max_length=254,null=False, primary_key = True)
    phone_no = models.CharField(max_length=13,null=False)
    birth_date = models.DateField(null=True,blank = False)
    objects = UserManager()

    @property
    def is_superuser(self):
    	return self.superuser
    
	@property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_active(self):
        return self.active

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
	#Research Areas?
	#Add fields accordingly

class ManagementPerson(models.Model):
	user = models.OnetotOneField(User,on_delete = models.CASCADE)

	#ManagementPerson will be specific to one institute.
	college = models.ForeignKey(College, on_delete = models.CASCADE)

	#position choices and position attribute
	#add more fields accordingly
	DEPARTMENT_CHOICES = (
		(FINANCE, "Finance"),
		(ACADEMICS, "Academics")
		)
	department = CharField(
		max_length=20,
		choices = DEPARTMENT_CHOICES,
		default = None
		)
	#Add fields accordingly