import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()  # charge les variables d'environnement à partir du fichier .env
api_key = os.getenv('API_KEY')  # récupère la valeur de la variable d'environnement API_KEY


# fonction pour récupérer les données météorologiques pour une ville donnée
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None

# définition de l'application Streamlit
def app():
    st.title('Informations météorologiques')

    # sélection de la ville avec autocomplétion
    city_list = [ 'Paris','Autre', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille']
    city = st.selectbox('Sélectionnez une ville', city_list + ['Autre'])

    if city == 'Autre':
        # saisie manuelle d'une ville
        city = st.text_input('Entrez le nom de la ville')
    
    # récupération des données météorologiques pour la ville sélectionnée
    weather_data = get_weather(city)

    if weather_data:
        # affichage des informations météorologiques sous forme de métriques
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Température actuelle", value=f"{weather_data['main']['temp']} °C")
        with col2:
            st.metric(label="Température ressentie", value=f"{weather_data['main']['feels_like']} °C")
        with col3:
            st.metric(label="Vitesse du vent", value=f"{weather_data['wind']['speed']} m/s")

        # affichage des autres informations météorologiques
        st.write(f"**Ville :** {city}")
        st.write(f"**Température minimale :** {weather_data['main']['temp_min']} °C")
        st.write(f"**Température maximale :** {weather_data['main']['temp_max']} °C")
        st.write(f"**Pression atmosphérique :** {weather_data['main']['pressure']} hPa")
        st.write(f"**Humidité :** {weather_data['main']['humidity']} %")
        st.write(f"**Direction du vent :** {weather_data['wind']['deg']} °")
    else:
        st.write("Impossible de récupérer les données météorologiques pour cette ville.")

app()
