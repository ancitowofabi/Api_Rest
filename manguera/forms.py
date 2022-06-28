from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Item,Cliente


class ItemForm(forms.ModelForm):
    
    class Meta: 
        model= Item
        fields = ['name', 'desc', 'img']
        labels ={
            'name': 'Nombre', 
            'desc': 'Descripción',     
            'img': 'Imagen',     
        }
        widgets={
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese name', 
                    'name': 'name'
                }
            ), 
            'desc': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese desc', 
                    'name': 'desc'
                }
            ), 
            'img': forms.ClearableFileInput(attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese img', 
                    'name': 'img'
                }), 
            
        }
class ClienteForm(forms.ModelForm):
    
    class Meta: 
        model= Cliente
        fields = ['rut','name','correo','fono','direccion']
        labels ={
            'rut' : 'Rut',
            'name' : 'Nombre',
            'correo' : 'Correo',
            'fono' : 'Teléfono',
            'direccion' : 'Dirección'
        }
        widgets={
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese name', 
                    'name': 'name'
                }
            ),          
        }
