from django.forms import ModelForm
from .models import ride
from django import forms

class RideForm(ModelForm):
    class Meta:
        model = ride
        fields = [
            'car_type',
            'car_pickup',
            'car_drop',
        ]
        widgets = {

            'car_type' : forms.Select(attrs = {'class' : 'form-control'},),
            'car_pickup' : forms.Select(attrs = {'class' : 'form-control'},),
            'car_drop' : forms.Select(attrs = {'class' : 'form-control'},)
        }
