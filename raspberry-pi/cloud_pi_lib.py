import requests
import cv2
import base64
import os
import json

api_key = os.getenv('CLOUD_PROZ_API')

def api_key_check():
    if not api_key:
        print('API key not found')
        return False
    return True

def send_image_for_processing(image):
    
    if not api_key_check():
        print('You need to run the command: export CLOUD_PROZ_API=<your_api_key>')
        return {"Error": "API key not found"}
    

    # Prepare the request payload
    payload = {
        "collection_name": "collection1",
        "photo_byte": image
    }

    # API endpoint
    url = 'https://bhc4ubyma7.execute-api.us-east-2.amazonaws.com/mirainixA/facesearch_base64'

    headers = {
        'x-api-key': api_key
    }

    # Send the request
    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def draw_bounding_box(image, response, img_width, img_height):
    
    for match in response.get('FaceMatches', []):
        # Get the bounding box
        box = match['Face']['BoundingBox']
        # img_height, img_width, _ = image.shape
        
        # Calculate the coordinates
        x1, y1, x2, y2 = (int(box['Left'] * img_width), 
                          int(box['Top'] * img_height), 
                          int((box['Left'] + box['Width']) * img_width), 
                          int((box['Top'] + box['Height']) * img_height))

        # Draw the rectangle
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Put the label
        label = match['Face'].get('ExternalImageId', 'Unknown')
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


def api(img_pipe, api_pipe):
    while True:
        # Read the latest image from img_pipe
        with open(img_pipe, 'r') as f:
            frame = f.read()
            # print(frame)

        # Process the image
        # try:
        response = send_image_for_processing(frame)
        response = str(response).replace("'",'"')
        print(response)
        # except:
        #     response = b''

        # Write the result to api_pipe
        with open(api_pipe, 'w') as f:
            f.write(response)
            # print(response)

def camera_function(picam2, img_pipe, api_pipe):
    frame = picam2.capture_array()

    retval, buffer = cv2.imencode('.jpg', frame)
# # Convert to base64 encoding and decode to get the string representation
    jpg_as_text = base64.b64encode(buffer).decode()


    # Write frame to img_pipe for processing
    with open(img_pipe, 'w') as f:
        f.write(jpg_as_text)

    # Read the latest bounding box data from api_pipe
    try:
        with open(api_pipe, 'r') as f:
            response = json.load(f)

    except Exception as e:
        response = None
    return frame, response

