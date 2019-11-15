from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from myapp.models import User, Professors, Directors, Staff, Admin


class ProfessorsCreationForm(UserCreationForm):

    visitingFaculty = forms.BooleanField(default=false)

	department = forms.ChoiceField(
							widget=forms.Select(),
							required=True
							)

	research_areas = forms.CharField(max_length=2000)

    class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + \
		    ('first_name', 'last_name', 'phone_no')

    @transaction.atomic
    def save(self):
        user.save()
        prof = Professors.objects.create(
        							user=user,
        							college=self.instance.user.college,
        							visitingFaculty=visitingFaculty,
        							department=department,
        							research_areas=research_areas
        							)
        prof.groups.add('professors')
        return user


class DirectorsCreationForm(UserCreationForm):

	mentor = forms.ChoiceField(
							widget=forms.Select(),
							required=True
							)

	class Meta(UserCreationForm.Meta):
		model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'phone_no')

	@transaction.atomic
	def save(self):
		user.save()
        director = Directors.objects.create(
        							user=user,
        							college=self.instance.user.college,
        							mentor=mentor,
        							)
		return user


class StaffCreationForm(UserCreationForm):

	department = forms.ChoiceField(
							widget=forms.Select(),
							required=True
							)

    class Meta( UserCreationForm.Meta ):
		model = User
        fields = UserCreationForm.Meta.fields + ( 'first_name', 'last_name', 'phone_no' )

    @transaction.atomic
    def save(self):
        user.save()
        staff = Staff.objects.create(
        							user = user,
        							college = self.instance.user.college,
        							department = department
        							)
        staff.groups.add( 'staff' )
        return user

class AdminCreationForm( UserCreationForm ):

    class Meta( UserCreationForm.Meta ):
        model = User
        fields = UserCreationForm.Meta.fields + ( 'first_name', 'last_name', 'phone_no' )
