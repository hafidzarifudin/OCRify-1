from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from .ocr import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = OCRInputForm(request.POST, request.FILES)
        if form.is_valid():
            #ocr_result = sendOCR(form['input_img'])
            return render('success')
    else:
        form = OCRInputForm()   
    return render(request, 'image_form.html', {'form' : form})

def success(request):
    return HttpResponse('Nice')
 