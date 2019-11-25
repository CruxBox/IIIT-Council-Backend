from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.http import HttpResponse
# guardian
# from guardian.shortcuts import assign_perm

from guardian.decorators import permission_required_or_403
from guardian.mixins import PermissionRequiredMixin


# A template of how the views are made
#
# class ProfessorView(PermissionRequiredMixin, View):
#
# 	#This checks to confirm that request.user has the required permissions
# 	permission_required = 'users.add_Professor'
#	instance.groups.add(group_name) #instance is the newly created professor instance
#
################


# class ProfessorAddView(PermissionRequiredMixin, View):

# 	#This checks to confirm that request.user has the required permissions
# 	permission_required = 'users.add_Professor'

# instance.groups.add('professors')

# add director
# add staff
# delete functions
# change functions
class CreateDirectorView(PermissionRequiredMixin, View):
    permission_required_or_403 = 'users.add_Director'

    def get(self, request):
        form = DirectorsCreationForm()
        return render(request, 'test.html', {'form': form})

    def post(self, request):
        form = DirectorsCreationForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return HttpResponse("<h2>Director Created Successfully</h2>")


class CreateStaffView(PermissionRequiredMixin, View):
    permission_required_or_403 = 'users.add_Staff'

    def get(self, request):
        form = StaffCreationForm()
        return render(request, 'test.html', {'form': form})

    def post(self, request):
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return HttpResponse("<h2>Staff Created Successfully</h2>")


class CreateProfessorView(PermissionRequiredMixin, View):
    permission_required_or_403 = 'users.add_Professor'

    def get(self, request):
        form = ProfessorsCreationForm()
        return render(request, 'test.html', {'form': form})

    def post(self, request):
        form = ProfessorsCreationForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return HttpResponse("<h2>Professor Created Successfully</h2>")
