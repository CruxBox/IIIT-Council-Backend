from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *
from users.forms import DirectorsCreationForm,StaffCreationForm
# Register your models here.
#admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Directors)
admin.site.register(Professors)



class CustomUserAdmin(UserAdmin):
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User,CustomUserAdmin)
admin.site.register(Staff)