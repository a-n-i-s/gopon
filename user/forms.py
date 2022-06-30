from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from django import forms

class UserCreateForm(ModelForm):
  password1=forms.CharField(label='password',widget=forms.PasswordInput)
  password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)
  
  class Meta:
    model=User
    fields=['email']
  def clean_password2(self):
    password1=self.cleaned_data.get('password1','')
    password2=self.cleaned_data.get('password2','')
    if password1!=password2:
      raise ValueError("Both passwords don't match.")
    return password2

  def save(self,commit=True):
    user=super().save(commit=False)
    user.set_password(self.cleaned_data.get('password1'))
    if commit:
      user.save()
    return user

class UserChangeForm(ModelForm):
  password=ReadOnlyPasswordHashField()
  class Meta:
    model=User
    fields=['email','password']
  