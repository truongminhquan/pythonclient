import logging.config
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
import json
from flask import make_response
from urllib.parse import urljoin

app = Flask(__name__)


@app.route('/')
def home():
    #put your live url here
    request_url = "https://functionapptodeploy1234.azurewebsites.net/api/"
    
    response = requests.get(request_url + 'getnotes')
    posts = response.json()
    print("================Result" + str(posts))
    return render_template("index.html", posts=posts)

def main():
    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    main()
