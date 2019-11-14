from django.shortcuts import render
from django.views import View

#guardian
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import assign_perm
from guardian.mixin import PermissionRequiredMixin


################ A template of how the views are made
#
# class ProfessorView(PermissionRequiredMixin, View):
#
# 	#This checks to confirm that request.user has the required permissions
# 	permission_required = 'users.add_Professor'
#	instance.groups.add(group_name) #instance is the newly created professor instance
#
################


class ProfessorAddView(PermissionRequiredMixin, View):

	#This checks to confirm that request.user has the required permissions
	permission_required = 'users.add_Professor'


	#instance.groups.add('professors')

#add director
#add staff
#delete functions
#change functions
