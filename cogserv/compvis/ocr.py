from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import io
import os
from PIL import Image
import requests
import sys
import time

subscription_key = "1b96e7f1dcd0473cb540714720ac6641"
endpoint = "https://dydx-computervision.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def sendOCR(image):
    print(image.format)
    out = io.BytesIO()
    image.save(out, format = image.format)
    image_in_bytes = out.getvalue()

    return image_in_bytes

    read_response = computervision_client.read_in_stream(image_in_bytes,  raw=True)

    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Process results

    #######################
    # Modify as necessary #
    #######################
    text_result = []
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text)
                print(line.bounding_box)
                text_result.append(line.text)
