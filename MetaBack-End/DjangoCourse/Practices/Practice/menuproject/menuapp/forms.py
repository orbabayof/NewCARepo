from django import forms
from .models import formModel

class Form(forms.ModelForm):
     class Meta:
          model = formModel
          fields =  '__all__'