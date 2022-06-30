from dataclasses import fields
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreateForm,UserChangeForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
  form=UserChangeForm
  add_form=UserCreateForm
  ordering=('email',)
  list_display=['email','is_superuser']
  list_filter=['is_superuser']
  fieldsets=[
    (None,{'fields':['email','password','is_superuser']}),
  ]
  

  add_fieldsets=[
    (None,{
      'fields':['email','password1','password2']
      }),
  ]


admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
