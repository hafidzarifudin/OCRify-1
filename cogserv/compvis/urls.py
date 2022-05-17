from django.urls import path
from .views import ocr_api, temp_api

urlpatterns = [
    path('', ocr_api.urls),
    path('success/', temp_api.urls, name='success')
]