from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect,render
from ninja import NinjaAPI
from PIL import Image
from .forms import *
from .ocr import *

ocr_api = NinjaAPI(urls_namespace='ocr_api')
temp_api = NinjaAPI(urls_namespace='temp_api')

# Create your views here.
@ocr_api.get('/')
def index(request):
    form = OCRInputForm()
    return render(request, 'image_form.html', {'form' : form})

@ocr_api.post('/')
def ocr_post(request):
    form = OCRInputForm(request.POST, request.FILES)
    if form.is_valid():
        ocr_result = sendOCR(Image.open(request.FILES['input_img']))
        #Undefined OCR processing

        #Temporary render
        return redirect('/success/')
    else:
        messages.error(request, 'Please submit a valid image file')
        
@temp_api.get('/')
def success(request):
    return HttpResponse('Nice')
 