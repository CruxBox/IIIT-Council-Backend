# Generated by Django 2.2.6 on 2019-11-16 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'default_permissions': (), 'permissions': [('view_Admin', 'Can view admin'), ('add_Admin', 'Can add admin'), ('change_Admin', 'Can change admin'), ('delete_Admin', 'Can delete admin')]},
        ),
        migrations.AlterModelOptions(
            name='directors',
            options={'default_permissions': (), 'permissions': [('view_Director', 'Can view director'), ('add_Director', 'Can add director'), ('change_Director', 'Can change director'), ('delete_Director', 'Can delete director')]},
        ),
        migrations.AlterModelOptions(
            name='professors',
            options={'default_permissions': (), 'permissions': [('view_Professor', 'Can view professor'), ('add_Professor', 'Can add professor'), ('change_Professor', 'Can change professor'), ('delete_Professor', 'Can delete professor')]},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'default_permissions': (), 'permissions': [('view_Staff', 'Can view staff'), ('add_Staff', 'Can add staff'), ('change_Staff', 'Can change staff'), ('delete_Staff', 'Can delete staff')]},
        ),
    ]
