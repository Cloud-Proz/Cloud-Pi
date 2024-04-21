import requests
import os
import sys
from io import BytesIO
import base64
import json

#api_key = os.getenv('CLOUD_PROZ_API')
f = open('config.json')
data = json.load(f)
#api_key = os.getenv('CLOUD_PROZ_API')
api_key = data['CLOUD_PROZ_API']

MIN_ARG_COUNT = 4

if not api_key:
    print('API key not found')
    sys.exit(1)

if len(sys.argv) < MIN_ARG_COUNT:
    print(f'Usage: {sys.argv[0]} <collection_name> <photo_id> <photo_path>')
    sys.exit(1)


def addface(collection_name, user_id, photo_path):
    
    try:
        # Open and read the image file
        with open(photo_path, 'rb') as image_file:
            jpg_as_text = base64.b64encode(image_file.read()).decode()
    except Exception as e:
        return {"error": f"Failed to process image: {str(e)}"}


    # Prepare the request payload
    payload = {
        "collection_name": collection_name,
        "photo_id": user_id,
        "photo_byte": jpg_as_text
    }

    # API endpoint
    url = 'https://bhc4ubyma7.execute-api.us-east-2.amazonaws.com/mirainixA/addface_base64'

    headers = {
        'x-api-key': api_key
    }

    # Send the request
    response = requests.post(url, headers=headers, json=payload)

    try:
        return response.json()
    except:
        return response.text


result = addface(sys.argv[1], sys.argv[2], sys.argv[3])
print(result)