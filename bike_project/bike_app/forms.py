from django import  forms
from . models import  New_bikes

class UPbike(forms.ModelForm):
    class Meta:
        model=New_bikes
        fields=['name','brand','img','price']