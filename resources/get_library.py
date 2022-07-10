import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

auth = os.environ["gist_token"]

def get_library():
    gist = requests.get("https://api.github.com/gists/de4f6f7328c06e1d6d33201a64778288", headers={"Authorization": f"token {auth}"}).json()
    content = gist["files"]["library.json"]["content"]
    return json.loads(content)
