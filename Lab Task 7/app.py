from flask import Flask, render_template
import requests

app = Flask(__name__)

NASA_API = "PQJ1o3eHjBHbKQhYZOXMkFDubNXCkbFdqhDHMLOv"
APOD_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=PQJ1o3eHjBHbKQhYZOXMkFDubNXCkbFdqhDHMLOv"

@app.route("/", methods=["GET"])
def index():
    params = {"api_key": NASA_API} 
    response = requests.get(APOD_URL, params=params)  
    apod_data = response.json()

    return render_template("index.html", apod=apod_data)

if __name__ == "__main__":
    app.run(debug=False)
