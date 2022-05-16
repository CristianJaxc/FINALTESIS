from django import forms

from .models import Order

from crispy_forms.helper import FormHelper
class OrderCreateForm(forms.ModelForm):


    class Meta:
        model = Order

        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code',
                  'city']


    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese tu nombre','label':'Nombre'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu apellido'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Ingrese un correo electronico '}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu direccion  '}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el codigo Postal'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la ciudad '}))

