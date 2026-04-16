#!/usr/bin/env python3
"""
Exemples avancés d'utilisation du DHT11
"""

import time
import board
import adafruit_dht
from datetime import datetime

# Configuration
DHT_PIN = board.D4

# ========================================
# EXEMPLE 1 : Lecture unique
# ========================================
def lecture_unique():
    """Effectue une seule lecture du capteur"""
    dht = adafruit_dht.DHT11(DHT_PIN)
    try:
        temp = dht.temperature
        hum = dht.humidity
        print(f"Température: {temp}°C, Humidité: {hum}%")
    finally:
        dht.exit()


# ========================================
# EXEMPLE 2 : Alerte température
# ========================================
def alerte_temperature(seuil_max=30, seuil_min=15):
    """Alerte si la température dépasse les seuils"""
    dht = adafruit_dht.DHT11(DHT_PIN)
    print(f"Surveillance de température (min: {seuil_min}°C, max: {seuil_max}°C)")
    print("Ctrl+C pour arrêter\n")
    
    try:
        while True:
            try:
                temp = dht.temperature
                hum = dht.humidity
                
                if temp > seuil_max:
                    print(f"⚠️  ALERTE: Température élevée! {temp}°C (humidité: {hum}%)")
                elif temp < seuil_min:
                    print(f"❄️  ALERTE: Température basse! {temp}°C (humidité: {hum}%)")
                else:
                    print(f"✓ OK: {temp}°C, {hum}%")
                
            except RuntimeError as e:
                print(f"Erreur lecture: {e}")
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nArrêt...")
    finally:
        dht.exit()


# ========================================
# EXEMPLE 3 : Calcul du point de rosée
# ========================================
def calculer_point_rosee(temperature, humidite):
    """
    Calcule le point de rosée approximatif
    Formule de Magnus-Tetens
    """
    a = 17.27
    b = 237.7
    
    alpha = ((a * temperature) / (b + temperature)) + (humidite / 100.0)
    point_rosee = (b * alpha) / (a - alpha)
    
    return round(point_rosee, 1)


def afficher_avec_point_rosee():
    """Affiche température, humidité et point de rosée"""
    dht = adafruit_dht.DHT11(DHT_PIN)
    print("=== Mesures complètes avec point de rosée ===\n")
    
    try:
        while True:
            try:
                temp = dht.temperature
                hum = dht.humidity
                point_rosee = calculer_point_rosee(temp, hum)
                
                print(f"Température: {temp}°C")
                print(f"Humidité: {hum}%")
                print(f"Point de rosée: {point_rosee}°C")
                print("-" * 40)
                
            except RuntimeError as e:
                print(f"Erreur: {e}")
            
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\nArrêt...")
    finally:
        dht.exit()


# ========================================
# EXEMPLE 4 : Statistiques sur période
# ========================================
def statistiques(duree_minutes=5):
    """Calcule min, max, moyenne sur une période"""
    dht = adafruit_dht.DHT11(DHT_PIN)
    temperatures = []
    humidites = []
    
    print(f"=== Collecte de données pendant {duree_minutes} minutes ===\n")
    
    debut = time.time()
    fin = debut + (duree_minutes * 60)
    
    try:
        while time.time() < fin:
            try:
                temp = dht.temperature
                hum = dht.humidity
                
                temperatures.append(temp)
                humidites.append(hum)
                
                temps_restant = int((fin - time.time()) / 60)
                print(f"[{len(temperatures)} lectures] {temp}°C, {hum}% - {temps_restant}min restantes")
                
            except RuntimeError as e:
                print(f"Erreur: {e}")
            
            time.sleep(10)  # Lecture toutes les 10 secondes
        
        # Afficher les statistiques
        print("\n" + "=" * 50)
        print("STATISTIQUES")
        print("=" * 50)
        print(f"Nombre de lectures: {len(temperatures)}")
        print(f"\nTempérature:")
        print(f"  Min: {min(temperatures)}°C")
        print(f"  Max: {max(temperatures)}°C")
        print(f"  Moyenne: {sum(temperatures)/len(temperatures):.1f}°C")
        print(f"\nHumidité:")
        print(f"  Min: {min(humidites)}%")
        print(f"  Max: {max(humidites)}%")
        print(f"  Moyenne: {sum(humidites)/len(humidites):.1f}%")
        
    except KeyboardInterrupt:
        print("\nInterrompu par l'utilisateur")
    finally:
        dht.exit()


# ========================================
# EXEMPLE 5 : Confort thermique
# ========================================
def evaluer_confort():
    """Évalue le niveau de confort basé sur température et humidité"""
    dht = adafruit_dht.DHT11(DHT_PIN)
    print("=== Évaluation du confort thermique ===\n")
    
    try:
        while True:
            try:
                temp = dht.temperature
                hum = dht.humidity
                
                # Critères de confort (simplifiés)
                if 18 <= temp <= 24 and 30 <= hum <= 60:
                    confort = "😊 CONFORTABLE"
                elif temp > 26:
                    confort = "🥵 TROP CHAUD"
                elif temp < 16:
                    confort = "🥶 TROP FROID"
                elif hum > 70:
                    confort = "💧 TROP HUMIDE"
                elif hum < 30:
                    confort = "🏜️  TROP SEC"
                else:
                    confort = "🙂 ACCEPTABLE"
                
                print(f"{datetime.now().strftime('%H:%M:%S')} - "
                      f"{temp}°C, {hum}% - {confort}")
                
            except RuntimeError as e:
                print(f"Erreur: {e}")
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nArrêt...")
    finally:
        dht.exit()


# ========================================
# MENU PRINCIPAL
# ========================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("EXEMPLES D'UTILISATION DHT11")
    print("=" * 50)
    print("\n1. Lecture unique")
    print("2. Alerte température")
    print("3. Point de rosée")
    print("4. Statistiques (5 minutes)")
    print("5. Évaluation confort")
    print("\n0. Quitter")
    
    choix = input("\nVotre choix: ")
    
    if choix == "1":
        lecture_unique()
    elif choix == "2":
        alerte_temperature()
    elif choix == "3":
        afficher_avec_point_rosee()
    elif choix == "4":
        statistiques()
    elif choix == "5":
        evaluer_confort()
    else:
        print("Au revoir!")
