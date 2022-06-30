from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
  def _create_user(self,email,password,**extra_fields):
    if not email:
      raise ValueError('You must provide an valid email.')
    email=self.normalize_email(email)
    user=self.model(email=email,**extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self,email,password,**extra_fields):
    extra_fields.setdefault('is_superuser',False)
    extra_fields.setdefault('is_staff',False)
    return self._create_user(email,password,**extra_fields)

  def create_superuser(self,email,password,**extra_fields):
    extra_fields.setdefault('is_superuser',True)
    extra_fields.setdefault('is_staff',True)
    if not extra_fields.get('is_superuser'):
      raise ValueError('superuser must have is_superuser=True')
    
    if not extra_fields.get('is_staff'):
      raise ValueError('superuser must have is_staff=True')
    
    return self.create_user(email,password,**extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):
  email=models.EmailField(unique=True)
  is_superuser=models.BooleanField(default=False)
  is_staff=models.BooleanField(default=False)
  objects=UserManager()
  USERNAME_FIELD='email'
  REQUIRED_FIELDS=[]

  def __str__(self):
    return str(self.email)
  


