from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from PIL import Image
from .forms import *
from .ocr import *
from .text_to_speech import *
from .translator import *

context = {
    'result': '',
    'available_languages': available_languages,
    'source_language': 'en',
    'target_language': 'id'
}

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'image_form.html')

def ocr_post(request):
    if request.method == 'POST':
        form = OCRInputForm(request.POST, request.FILES)
        if form.is_valid():
            ocr_result = sendOCR(Image.open(request.FILES['input_img']))
            translation_result = translate(ocr_result, 'en', 'id')
            context['result'] = translation_result
        return render(request, 'image_form.html', context)

def translate_post(request):
    if request.method == 'POST':
        form = OCRInputForm(request.POST, request.FILES)
        if form.is_valid():
            ocr_result = sendOCR(Image.open(request.FILES['input_img']))
            translation_result = translate(ocr_result, 'en', 'id')
            context['result'] = translation_result
        return render(request, 'image_form.html', context)

def tts_post(request):
    if request.method == 'POST':
        pass