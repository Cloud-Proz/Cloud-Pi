import requests
import os
import sys

api_key = os.getenv('CLOUD_PROZ_API')

MIN_ARG_COUNT = 3

if not api_key:
    print('API key not found')
    sys.exit(1)

if len(sys.argv) < MIN_ARG_COUNT:
    print(f'Usage: {sys.argv[0]} <collection_name> <user_id>')
    sys.exit(1)


def create_collection(collection_name, user_id):

    # Prepare the request payload
    payload = {
        "collection_name": collection_name,
        "user_id": user_id
    }

    # API endpoint
    url = 'https://bhc4ubyma7.execute-api.us-east-2.amazonaws.com/mirainixA/createcollection'

    headers = {
        'x-api-key': api_key
    }

    # Send the request
    response = requests.post(url, headers=headers, json=payload)

    try:
        return response.json()
    except:
        return response.text


result = create_collection(sys.argv[1], sys.argv[2])
print(result)