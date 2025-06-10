# 🌤️ Flask Weather App

A simple Flask-based web application to fetch and display current weather information for any city using the [Weatherbit API](https://www.weatherbit.io/).

---

## 📸 Preview

![Weather App Screenshot](https://github.com/joise-s-arakkal/Weather-App/blob/main/static/Screenshot.PNG)

---

## 🚀 Features

- Search for current weather by city name  
- Fetches real-time weather data from Weatherbit API  
- Lightweight, responsive HTML interface  
- Built with Python, Flask, and Jinja2 templates

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/joise-s-arakkal/Weather-App.git
cd Weather-App
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up `.env` File
Create a .env file in the root directory with the following content:

```bash
WEATHER_API_KEY=your_weatherbit_api_key_here
```
> 🔑 You can obtain your free API key from [weatherbit](https://www.weatherbit.io/)

---

## 🚦 Running the App
```bash
python app.py
```
Visit [http://localhost:5050](http://localhost:5050) in your browser.

---

🌐 Made with ❤️ using Flask and Weatherbit API

