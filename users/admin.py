from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *
from users.forms import DirectorsCreationForm,StaffCreationForm
from django.contrib.auth.forms import UserCreationForm
# Register your models here.
#admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Directors)
admin.site.register(Professors)

class CustomUserAdmin(UserAdmin):
    #add_form = UserCreateForm
    #prepopulated_fields = {'username': ('first_name' , 'last_name', )}
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'email'),
        }),
    )

admin.site.register(User,CustomUserAdmin)
admin.site.register(Staff)