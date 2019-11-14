"""
Create permission groups
Create permissions (CRUD) for a set of groups. At the moment only one default group which comprises of admins and superusers exists.
"""

"""
Usage: manage.py create_groups
"""

import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from users.models import User

GROUPS = ['admins']
MODELS = User.objects.all()
PERMISSIONS = ['view', 'add', 'delete', 'change']

class Command(BaseCommand):
    help = 'Creates default permission groups for adminss'

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
            	#check if admin then continue
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