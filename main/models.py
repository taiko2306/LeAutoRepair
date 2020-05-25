from django.db import models

class Vehicle(models.Model):
    vin = models.CharField(max_length=20, unique=True)
    reg_number = models.CharField(max_length=30, null=True, blank=True)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.vin + ' | ' + self.make + ' | ' + self.model + ' | ' + self.year

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

    def save(self, *args, **kwargs):
        self.vin = str(self.vin).upper()
        self.reg_number = str(self.reg_number).upper()
        return super(Vehicle, self).save(*args, **kwargs)