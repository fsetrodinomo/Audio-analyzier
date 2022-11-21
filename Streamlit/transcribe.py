import os
from dotenv import load_dotenv
import requests

#Helper function: uploading a local audio file to API
# Post request to API endpoint
# deleted after transcription never stored


def get_url(token,data):
    headers = {'authorization' : token}
    response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=data)
    url = response.json()["upload_url"]
    print("Uploaded file and got temporary URL to file")
    return url

#upload file trancstription
def get_transcribe_id(token,url):
    endpoint ="https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url" :  url
    }
    headers = {
        "authorization" : token,
        "content-type" : "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    id = response.json() ['id']
    print("Made request and file is currently queued")
    return id