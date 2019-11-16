"""
This management command creates permission groups
Creates CRUD permissions for admins.
Creates view permission for professor and staff.

Director isn't added to any group at the moment. Permissions are defined in Director model. Which group he belongs to is up for discussion.
"""

"""
Usage: manage.py create_groups
"""


import logging
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
GROUPS = ['admins', 'professors', 'staff', ]
# If more models are create they need to be added in this list
MODELS = ['professor', 'director', 'staff', ]
PERMISSIONS = ['view', 'add', 'delete', 'change', ]
PERMISSIONS_LIMIT = ['view', ]


class Command(BaseCommand):
    help = 'Creates default permission groups for admins, professors and staff'

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
                if group != 'admins':
                    for permission in PERMISSIONS_LIMIT:
                        name = 'Can {} {}'.format(permission, model)
                        print("Creating {}".format(name))

                        try:
                            model_add_perm = Permission.objects.get(name=name)
                        except Permission.DoesNotExist:
                            logging.warning(
                                "Permission not found with name '{}'.".format(name))
                            continue

                        new_group.permissions.add(model_add_perm)
                else:
                    for permission in PERMISSIONS:
                        name = 'Can {} {}'.format(permission, model)
                        print("Creating {}".format(name))

                        try:
                            model_add_perm = Permission.objects.get(name=name)
                        except Permission.DoesNotExist:
                            logging.warning(
                                "Permission not found with name '{}'.".format(name))
                            continue

                        new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")
