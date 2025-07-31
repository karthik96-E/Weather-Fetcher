from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# Add your actual API key here or use environment variable
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "78887c76d179e15f6feb670c19120235")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/weather", methods=["POST"])
def get_weather():
    data = request.get_json()
    city = data.get("city", "")
    if not city:
        return jsonify({"error": "City name is required"}), 400
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        # 👇 Print the real error to terminal for debugging
        print("Error from OpenWeatherMap:", response.status_code, response.text)
        return jsonify({"error": "Could not fetch weather"}), 500
    
    weather_data = response.json()
    result = {
        "city": weather_data.get("name"),
        "temperature": weather_data["main"]["temp"],
        "description": weather_data["weather"][0]["description"],
        "humidity": weather_data["main"]["humidity"]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
