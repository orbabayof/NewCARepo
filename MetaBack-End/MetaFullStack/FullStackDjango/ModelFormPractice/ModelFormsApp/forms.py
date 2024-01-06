from .models import Logger
from django import forms

class LoggerForm(forms.ModelForm):
     class Meta:
          model = Logger
          fields = '__all__'