#!/usr/bin/env python3
"""
Script de lecture du capteur DHT11
Récupère la température et l'humidité
"""

import time
import board
import adafruit_dht

# Configuration du capteur DHT11
# Changez le pin selon votre branchement (D4 = GPIO 4)
# Pins disponibles : board.D4, board.D17, board.D18, etc.
DHT_PIN = board.D4

# Initialiser le capteur DHT11
dht_device = adafruit_dht.DHT11(DHT_PIN)

print("=== Capteur DHT11 - Lecture de température et humidité ===")
print("Appuyez sur Ctrl+C pour arrêter\n")

try:
    while True:
        try:
            # Lecture de la température et de l'humidité
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            
            # Affichage des résultats
            print(f"Température: {temperature_c:.1f}°C | Humidité: {humidity:.1f}%")
            
        except RuntimeError as error:
            # Les erreurs de lecture sont courantes avec le DHT11
            # On les ignore et on réessaye
            print(f"Erreur de lecture: {error.args[0]}")
            time.sleep(2.0)
            continue
        except Exception as error:
            dht_device.exit()
            raise error
        
        # Attendre 2 secondes avant la prochaine lecture
        # Le DHT11 ne peut pas être lu plus vite que toutes les 2 secondes
        time.sleep(2.0)

except KeyboardInterrupt:
    print("\n\nArrêt du programme...")
    dht_device.exit()
    print("Programme terminé.")
