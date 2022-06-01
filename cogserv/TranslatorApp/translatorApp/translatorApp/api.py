from ninja import NinjaAPI
from django.http import HttpRequest
import requests, uuid, json

api = NinjaAPI()

'''
To get the result of translation, go to http://127.0.0.1:8000/api/translate endpoint
'''

@api.get("/translate")
def translate(request:HttpRequest):
    # Add your key and endpoint
    key = '5a7f1acf4c6847a6b2e26b74835afd80'
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = 'eastus'
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': ['de', 'it'] # take input from user 
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': 'Saya suka makan nasi goreng' # take input from OCR
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response[0] 

