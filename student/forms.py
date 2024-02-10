from django import forms
from django.forms import ModelForm
from .models import *
from .choices import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username','password1','password2','user_selenium','password_selenium','grade','password','email']



class RegisterForm(UserCreationForm):

    
    class Meta:
        model = Student
        fields = ['username','password1','password2','user_selenium','password_selenium','grade','email']
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2':None,
        }
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    