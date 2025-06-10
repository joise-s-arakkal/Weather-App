from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request
import os

load_dotenv()  # Load variables from .env
app = Flask(__name__)

def get_weather_data(city):
    base_url = "https://api.weatherbit.io/v2.0/current"
    api_key = os.getenv("WEATHER_API_KEY")
    params = {
            "key": api_key,
            "city": city,
            }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

@app.route('/', methods=['POST', 'GET'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        print(city)
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True,port=5050)