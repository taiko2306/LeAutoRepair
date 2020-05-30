from django import forms
from django.forms import ModelForm
from .models import Vehicle, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(ModelForm):
     class Meta:
        model = Profile
        fields = ['image']

#class Profile_Form(ModelForm):
#    class Meta:
#        model = User_Profile
#        fields = [
#        'fname',
#        'lname',
#        'title',
#        'email',
#        'display_picture',
#        ]
#        labels = {
#            "fname": "First Name",
#            "lname": "Last Name",
#            "title": "Title",
#            "email": "Email",
#            "display_picture": "Picture",
#        }

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle

        fields = [
            "vin",
            "reg_number",
            "make",
            "model",
            "year",
            "color",
            "image",
        ]
        labels = {
            "vin": "VIN",
            "reg_number": "Reg. #",
            "make": "Make",
            "model": "Model",
            "year": "Year",
            "color": "Color",
            "image": "Image",
        }

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
