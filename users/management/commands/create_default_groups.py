"""
Create permission groups
Create permissions (CRUD) for a set of groups. At the moment only one default group which comprises of admins and superusers exists.
Director isn't added to any group. Permissions are defined in Director model. Admin makes him a 
"""

"""
Usage: manage.py create_groups
"""

import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

GROUPS = ['admins', 'professors', 'staff',]
MODELS = ['professors', 'director', 'staff',] #If more models are create they need to be added in this list
PERMISSIONS = ['view', 'add', 'delete', 'change',]
PERMISSIONS_LIMIT = ['view',]

class Command(BaseCommand):
    help = 'Creates default permission groups for adminss'

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
            	if group not 'admins':
            		for permission in PERMISSIONS_LIMIT:
	                    name = 'Can {} {}'.format(permission, model)
	                    print("Creating {}".format(name))

	                    try:
	                        model_add_perm = Permission.objects.get(name=name)
	                    except Permission.DoesNotExist:
	                        logging.warning("Permission not found with name '{}'.".format(name))
	                        continue

	                    new_group.permissions.add(model_add_perm)
                else:
                	for permission in PERMISSIONS:
	                    name = 'Can {} {}'.format(permission, model)
	                    print("Creating {}".format(name))

	                    try:
	                        model_add_perm = Permission.objects.get(name=name)
	                    except Permission.DoesNotExist:
	                        logging.warning("Permission not found with name '{}'.".format(name))
	                        continue

	                    new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")