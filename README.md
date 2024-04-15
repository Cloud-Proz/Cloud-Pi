# Cloud-Pi

## user_tool_kit

**Note:** All operations below require the `CLOUD_PROZ_API` for authentication and access to the Cloud-Pi services
Once you have the API key, run this command in the terminal
export CLOUD_PROZ_API='API-KEY'


### File Descriptions

- `create_collection.py`: This file allows a user to create their face collections

- `delete_collection.py`: This file allows a user to delete their face collections

- `addface.py`: This file allows a user to add faces to their created collections
  - Pre-requisites:
    - A photo stored in your computer with a known path to the photo
    - It might be easier to just put the photo in user_tool_kit directory

## raspberry-pi

- `api.py`: This file needs to be running in the background for all the operations not in user_tool_kit
- `main.py`: This file is operating the camera and stream the result via flask onto a webbrowser
- `cloud_pi_lib.py`: This file contains pivotal functions for Cloud-Pi services


