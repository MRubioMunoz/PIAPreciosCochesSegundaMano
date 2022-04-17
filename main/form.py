from django import forms
from django.forms import ModelForm
from main.Tuplas import Tuplas


class Formulario(forms.Form):
    tuplas = Tuplas()
    km = forms.FloatField(label="Kilometros de su vehiculo")
    fuelTypeId = forms.ChoiceField(choices=tuplas.fuel, required=True, label="Tipo de combustible")
    makeId = forms.ChoiceField(choices=tuplas.marcas, label="Marca de su modelo")
    modelId = forms.ChoiceField(choices=tuplas.model, label="Modelo")    
    transmissionTypeId = forms.ChoiceField(choices=tuplas.transmissionTypeId, required=True, label="Tipo de vehiculo")
    year = forms.FloatField(label="Año del vehiculo")
    cubicCapacity = forms.FloatField(label="Centrimos cubicos del motor")
    door = forms.FloatField(label="Numero de puertas")
    hp = forms.FloatField(label="Caballos de Vapor (CV)")