from django.forms import ModelForm
from .models import Vehicle

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
