from django import forms
from .models import *

class OCRInputForm(forms.Form):
    input_img = forms.ImageField()