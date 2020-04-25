from django.db import models
from django.contrib.auth.models import User, auth
 
Pickup_Choices = (
    ('NHR', 'NHR'),
    ('AZD', 'AZD'),
    ('LBS', 'LBS'),
    ('MS', 'MS'),
    ('MMM', 'MMM'),
    ('BRH', 'BRH'),
    ('RK', 'RK'),
    ('RP', 'RP'),
    ('MT', 'MT'),
    ('SN', 'SN'),
    ('Airport', 'Airport'),
    ('KGP Railway', 'KGP Railway'),
    ('Hijli Railway', 'Hijli Railway'),


)

Drop_Choices = (
   ('NHR', 'NHR'),
    ('AZD', 'AZD'),
    ('LBS', 'LBS'),
    ('MS', 'MS'),
    ('MMM', 'MMM'),
    ('BRH', 'BRH'),
    ('RK', 'RK'),
    ('RP', 'RP'),
    ('MT', 'MT'),
    ('SN', 'SN'),
    ('Airport', 'Airport'),
    ('KGP Railway', 'KGP Railway'),
    ('Hijli Railway', 'Hijli Railway'),
)
car_types = (
    ('mini', 'mini'),
    ('micro', 'micro'),
    ('sedan', 'sedan'),
)
Approve_Choices = (
    ('approved', 'approved'),
    ('denied', 'denied'),
    ('not_confirmed', 'not_confirmed'),
)


class Car_location(models.Model):
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.location

class Car(models.Model):
    car_location = models.ForeignKey(Car_location, on_delete=models.CASCADE)
    driver = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    car_number = models.CharField(max_length=200)
    car_type = models.CharField(max_length=200, choices = car_types, default = None)
    is_available = models.BooleanField(default=True)
    is_running = models.BooleanField(default=False)
   

    def __str__(self):
        return self.car_type + '--' + self.car_number + '--' + self.car_model 

    


class ride(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, default = None, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=200, choices = car_types, default = 'sedan')
    car_pickup = models.CharField(max_length=200, choices = Pickup_Choices, default = 'AZD')
    car_drop = models.CharField(max_length=200, choices = Drop_Choices, default = 'LBS')
    is_approved = models.CharField(max_length=200, choices = Approve_Choices, default = 'not_confirmed')
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.car_type 

    @property
    def sorted_set(self):
        return self.sorted_set.order_by('id')

