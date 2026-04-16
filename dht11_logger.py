#!/usr/bin/env python3
"""
Script avancé de lecture du capteur DHT11
Enregistre les données dans un fichier CSV
"""

import time
import board
import adafruit_dht
from datetime import datetime
import csv
import os

# Configuration
DHT_PIN = board.D4
CSV_FILE = "dht11_data.csv"
INTERVAL = 2  # Intervalle de lecture en secondes

# Initialiser le capteur DHT11
dht_device = adafruit_dht.DHT11(DHT_PIN)

# Créer le fichier CSV s'il n'existe pas
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Heure', 'Température (°C)', 'Humidité (%)'])

print("=== Capteur DHT11 - Enregistrement des données ===")
print(f"Fichier de sortie: {CSV_FILE}")
print(f"Intervalle: {INTERVAL} secondes")
print("Appuyez sur Ctrl+C pour arrêter\n")

lecture_count = 0

try:
    while True:
        try:
            # Lecture de la température et de l'humidité
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            
            # Date et heure actuelles
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")
            
            # Enregistrer dans le CSV
            with open(CSV_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([date_str, time_str, f"{temperature_c:.1f}", f"{humidity:.1f}"])
            
            lecture_count += 1
            
            # Affichage des résultats
            print(f"[{lecture_count}] {date_str} {time_str} - "
                  f"Température: {temperature_c:.1f}°C | Humidité: {humidity:.1f}%")
            
        except RuntimeError as error:
            print(f"Erreur de lecture: {error.args[0]}")
            time.sleep(INTERVAL)
            continue
        except Exception as error:
            dht_device.exit()
            raise error
        
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print(f"\n\nArrêt du programme...")
    print(f"Total de lectures: {lecture_count}")
    print(f"Données enregistrées dans: {CSV_FILE}")
    dht_device.exit()
    print("Programme terminé.")
