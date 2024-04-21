# Cloud-Pi

## user_tool_kit

**Note:** All operations below require the `CLOUD_PROZ_API` for authentication and access to the Cloud-Pi services
Once you have the API key, add it to `config.json` file in both `user_tool_kit` and `raspberry-pi` directories


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

## Newly flashed SSD card

1. Clone this repo with `git clone https://github.com/Cloud-Proz/Cloud-Pi.git`
2. Change directory into Cloud-Pi with `cd Cloud-Pi`
3. Copy and paste the following commands:
```
sudo apt update
sudo apt upgrade
sudo apt install -y python3-libcamera python3-kms++ libcap-dev
sudo apt install -y python3-prctl libatlas-base-dev ffmpeg libopenjp2-7 python3-pip
pip install -r requirements.txt --break-system-packages

```

