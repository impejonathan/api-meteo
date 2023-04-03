import sqlite3
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import pandas as pd


load_dotenv()

def save_weather_data_to_db(city):
    # Connexion à la base de données
    conn = sqlite3.connect('db_weather.db')
    c = conn.cursor()

    # Récupération des données météorologiques pour les 30 derniers jours
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    # URL de l'API OpenWeatherMap
    url = 'https://api.openweathermap.org/data/2.5/weather'

    # clé API OpenWeatherMap
    api_key = os.getenv('API_KEY')

    # Récupération des données pour chaque jour
    for date in (start_date + timedelta(n) for n in range(30)):
        params = {'q': city, 'appid': api_key, 'units': 'metric', 'lang': 'fr'}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()

            # Enregistrement des données dans la base de données
            c.execute("""
                INSERT INTO weather (ville, jour, température_actuelle, température_ressentie, temperature_minimale,
                temperature_maximale, pression_atmosphérique, humidite, vitesse_du_vent, direction_du_vent, lever_du_solei,
                coucher_du_soleil) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (city, date.strftime('%Y-%m-%d'), data['main']['temp'], data['main']['feels_like'], data['main']['temp_min'],
                data['main']['temp_max'], data['main']['pressure'], data['main']['humidity'], data['wind']['speed'],
                data['wind']['deg'], pd.to_datetime(data['sys']['sunrise'], unit='s').strftime('%H:%M:%S'),
                pd.to_datetime(data['sys']['sunset'], unit='s').strftime('%H:%M:%S'))
            )

    # Sauvegarde des modifications dans la base de données
    conn.commit()

    # Fermeture de la connexion à la base de données
    conn.close()


save_weather_data_to_db("lille")