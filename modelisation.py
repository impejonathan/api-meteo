import sqlite3

connexion = sqlite3.connect("db_weather.db")

curseur = connexion.cursor()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS weather(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ville TEXT NOT NULL,
                    jour datetime NOT NULL,
                    température_actuelle FLOAT NOT NULL,
                    température_ressentie FLOAT NOT NULL,
                    temperature_minimale FLOAT NOT NULL,
                    temperature_maximale FLOAT NOT NULL,
                    pression_atmosphérique FLOAT NOT NULL,
                    humidite FLOAT NOT NULL,
                    vitesse_du_vent FLOAT NOT NULL,
                    direction_du_vent FLOAT NOT NULL,
                    lever_du_solei datetime NOT NULL,
                    coucher_du_soleil datetime NOT NULL
                    
                    
                )
                
                """)

connexion.commit()

connexion.close()