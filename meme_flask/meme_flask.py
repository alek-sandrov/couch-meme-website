#!/bin/python
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.request("GET", url)
    print("Status Code:", response.status_code)  # Output the HTTP status code
    print("Response Text:", response.text)  # Output the raw response text

    try:
        json_data = json.loads(response.text)
        meme_large = json_data["preview"][-2]
        subreddit = json_data["subreddit"]
        return meme_large, subreddit
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return None, None



@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=8080)

