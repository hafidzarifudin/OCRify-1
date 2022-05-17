from django import forms
from .models import *

class OCRInputForm(forms.ModelForm):
    class Meta:
        model = OCRInput
        fields = ['input_img']
        required = ['input_img']