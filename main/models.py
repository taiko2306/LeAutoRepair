from django.db import models
from datetime import datetime

class User_Profile(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length = 30)
    title = models.CharField(max_length=30)
    email = models.EmailField(default = None)
    display_picture = models.FileField()

    def __str__(self):
        return self.fname

class Vehicle(models.Model):
    vin = models.CharField(max_length=20, unique=True)
    reg_number = models.CharField(max_length=30, null=True, blank=True)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    display_picture = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.vin + ' | ' + self.make + ' | ' + self.model + ' | ' + self.year + ' | ' + self.color

    #@property
    def get_last_service_date(self):
        return "2020-01-01"
    image = models.ImageField(upload_to='vehicle_image',null=True, blank=True, default='vehicle_image/placeholder.png')

    @property
    def imageURL(self):
        try:
            url = self.image.url
            print(url)
        except:
            url = '/images/placeholder.png'
        return url

    @property
    def pictureURL(self):
        try:
            url = self.display_picture.url
            print(url)
        except:
            url = ''
        return url
    def save(self, *args, **kwargs):
        self.vin = str(self.vin).upper()
        self.reg_number = str(self.reg_number).upper()
        return super(Vehicle, self).save(*args, **kwargs)

class Service(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=30)
    desc = models.TextField(max_length=180, null=True, blank=True)
    Odometer = models.IntegerField()
    serviced_by = models.CharField(max_length=30)
    serviced_date = models.DateField(default=datetime.now)

    def __str__(self):
        return str(self.id) + ' | ' + str(self.name)