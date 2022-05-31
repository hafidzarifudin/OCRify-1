from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from PIL import Image
from .forms import *
from .ocr import *

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'image_form.html')
    elif request.method == 'POST':
        form = OCRInputForm(request.POST)
        if form.is_valid():
            #ocr_result = sendOCR(Image.open(request.FILES['input-img']))
            #Undefined OCR processing

            #Temporary render

            context = {
                'result': 'test'
            }
            return render(request, 'image_form.html', context)
        else:
            return redirect('index')