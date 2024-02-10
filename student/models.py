from django.db import models
from .choices import grade
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone
from django_cryptography.fields import encrypt
# Create your models here.


class MyStudentManager(BaseUserManager):
    def create_user(self,username,password,password_selenium,grade,user_selenium,email):
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username = username,
            password_selenium=password_selenium,
            grade=grade,
            user_selenium=user_selenium,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,password_selenium,grade,user_selenium,email):
        user = self.create_user(
            username = username,
            password=password,
            password_selenium=password_selenium,
            grade=grade,
            user_selenium=user_selenium,
            email=email,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser):
    #Required
    email =  models.EmailField(verbose_name='email',max_length=60,unique=False)
    username = models.CharField(max_length=30,unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #Custom
    user_selenium = encrypt(models.CharField(max_length=9))
    password_selenium = encrypt(models.CharField(max_length=15,))
    grade = models.CharField(choices=grade,default=1,max_length=2)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password_selenium','grade','user_selenium','email']

    objects = MyStudentManager()

    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
