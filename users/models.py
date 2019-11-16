from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_no']

    # attributes
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone_no = models.CharField(max_length=13, null=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Admin(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey('colleges.College', on_delete=models.CASCADE)

    class Meta:
        default_permissions = ()
        permissions = [
            ("view_Admin", "Can view admin"),
            ("add_Admin", "Can add admin"),
            ("change_Admin", "Can change admin"),
            ("delete_Admin", "Can delete admin"),
        ]


class Professors(models.Model):
    DEPARTMENT_CHOICES = (
        (1, "CSE"),
        (2, "ECE")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    visitingFaculty = models.BooleanField(default=False)

    colleges = models.ForeignKey('colleges.College', on_delete=models.CASCADE)

    # add more fields accordingly
    research_areas = models.CharField(max_length=2000)

    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES,
        default=None
    )

    class Meta:
        default_permissions = ()

        permissions = [
            ("view_Professor", "Can view professor"),
            ("add_Professor", "Can add professor"),
            ("change_Professor", "Can change professor"),
            ("delete_Professor", "Can delete professor"),
        ]
    # Add fields accordingly


class Directors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mentor = models.BooleanField(default=False)

    college = models.ForeignKey('colleges.College', on_delete=models.CASCADE)

    """
	
	if a professor, add one to one field with director
	is_professor = models.BooleanField( default = false )
	professor = models.ForeignKey(Professor, on_delete = models.SET_NULL)
	Fix this issue

	"""

    class Meta:
        default_permissions = ()
        permissions = [
            ("view_Director", "Can view director"),
            ("add_Director", "Can add director"),
            ("change_Director", "Can change director"),
            ("delete_Director", "Can delete director"),
        ]
    # Add fields accordingly


class Staff(models.Model):

    # position choices and position attribute
    DEPARTMENT_CHOICES = (
        (1, "Finance"),
        (2, "Academics")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Staff will be specific to one institute.
    college = models.ForeignKey('colleges.College', on_delete=models.CASCADE)

    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES,
        default=None
    )

    # Add fields accordingly
    class Meta:
        default_permissions = ()
        permissions = [
            ("view_Staff", "Can view staff"),
            ("add_Staff", "Can add staff"),
            ("change_Staff", "Can change staff"),
            ("delete_Staff", "Can delete staff"),
        ]
