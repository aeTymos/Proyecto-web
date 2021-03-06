from django import forms
from django.core.validators import MaxValueValidator
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError
from datetime import date
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus.widgets import DatePickerInput
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=5, max_length=30)
    descripcion = forms.CharField(min_length=10, max_length= 80)
    precio = forms.IntegerField(min_value=1, max_value=200000)
    fecha_agregado = forms.DateField(validators=[MaxValueValidator(limit_value=date.today)])
    miniatura = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError('Ya hay un producto con este nombre')

        return nombre

    class Meta:

        model = Producto
        fields = '__all__'

        widgets = {
            'fecha_agregado': DatePickerInput()
        }

class CustomUserCreationForm(UserCreationForm):

    captcha = CaptchaField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]