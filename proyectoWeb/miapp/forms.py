from django import forms
from .models import Contacto, Producto

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            'fecha_agregado': forms.SelectDateWidget()
        }