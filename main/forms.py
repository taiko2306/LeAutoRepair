from django.forms import ModelForm
from .models import Vehicle, User_Profile


class Profile_Form(ModelForm):
    class Meta:
        model = User_Profile
        fields = [
        'fname',
        'lname',
        'title',
        'email',
        'display_picture',
        ]
        labels = {
            "fname": "First Name",
            "lname": "Last Name",
            "title": "Title",
            "email": "Email",
            "display_picture": "Picture",
        }

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
            'display_picture',
        ]
        labels = {
            "vin": "VIN",
            "reg_number": "Reg. #",
            "make": "Make",
            "model": "Model",
            "year": "Year",
            "color": "Color",
            "image": "Image",
            "display_picture": "Picture",
        }

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
