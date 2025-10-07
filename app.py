from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "717b64c259b63d6656a8032709d0a797"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    
    if (request.method == "POST"):
        city = request.form.get("city")
        url = f"{API_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        if (response.status_code == 200):
            data = response.json()
            weather = {
                "temp" : data["main"]["temp"],
                "pressure": data["main"]["pressure"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "location": f"{data['name']}, {data['sys']['country']}"
            }
            
        else:
            weather = {"error": "City not found."}
        
    return render_template("index.html", weather=weather)  

if __name__ == "__main__":
    app.run(debug=True)