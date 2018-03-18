from django import forms
from . import models
class Owner_Reg(forms.ModelForm):
    class Meta:
        model = models.Owners
        fields = '__all__'
