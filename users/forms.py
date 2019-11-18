from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import Group
from colleges.models import College
from .models import User, Professors, Directors, Staff, Admin

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_no')



class ProfessorsCreationForm(CustomUserCreationForm):

    visitingFaculty = forms.BooleanField(required=False)
    department = forms.ChoiceField(widget=forms.Select(),
                                    choices=Professors.DEPARTMENT_CHOICES 
                                    ,required=True)
    research_areas = forms.CharField(max_length=2000)

    @transaction.atomic
    def save(self,request):
        user = super(ProfessorsCreationForm, self).save(commit=False)
        user.save()
        prof = Professors.objects.create(
            user=user, 
            colleges=request.user.admin.college,
            visitingFaculty=self.cleaned_data['visitingFaculty'], 
            department=self.cleaned_data['department'], 
            research_areas=self.cleaned_data['research_areas'])
        #group = Group.objects.get(name='professors')
        #group.user_set.add(prof)
        return user


class DirectorsCreationForm(CustomUserCreationForm):

    mentor = forms.BooleanField(required=True,initial=False)

    @transaction.atomic
    def save(self,request=None):
        user = super(DirectorsCreationForm, self).save(commit=False)
        user.save()
        director = Directors.objects.create(
            user=user,
            college=request.user.admin.college,
            mentor=self.cleaned_data['mentor']
        )
        return user


class StaffCreationForm(CustomUserCreationForm):

    department = forms.ChoiceField(
        widget=forms.Select(),
        choices= Staff.DEPARTMENT_CHOICES,
        required=True
    )
        

    @transaction.atomic
    def save(self,request=None):
        user = super(StaffCreationForm, self).save(commit=False)
        user.save()
        staff = Staff.objects.create(
            user=user,
            college=request.user.admin.college,
            department=self.cleaned_data['department']
        )
        group = Group.objects.get(name='staff')
        staff.groups.add(group)
        return user


class AdminCreationForm(CustomUserCreationForm):
    
    colleges=College.objects.all()
    college=forms.ChoiceField(choices=colleges)

 
    @transaction.atomic
    def save(self):
        user=super(AdminCreationForm).save(commit=False)
        admin=Admin.objects.create(
            user=user,
            college=self.cleaned_data['college']
            )
        group = Group.objects.get(name='admins')
        user.groups.add(group)
        return user
