from django.shortcuts import render
from django.views import View

#guardian
from guardian.shortcuts import assign_perm
from guardian.mixin import PermissionRequiredMixin


################ A template of how the views are made
#
# class add_professor_view(PermissionRequiredMixin, View):
#
# 	#This checks to confirm that request.user has the required permissions
# 	permission_required = 'users.add_Professor'
#	instance.groups.add(group_name) #instance is the newly created professor instance
#
################


class add_professor_view(PermissionRequiredMixin, View):

	permission_required = 'users.add_Professor'
	#Now create a professor normally
	#add him to the group

	#instance.groups.add('professors')
