#!/usr/bin/env python3
import time
import board
import adafruit_dht

# Liste des GPIO à tester
gpios_a_tester = [
    ("D4", board.D4),
    ("D17", board.D17),
    ("D18", board.D18),
    ("D27", board.D27),
    ("D22", board.D22),
    ("D23", board.D23),
    ("D24", board.D24),
    ("D25", board.D25),
]

print("=== Test de détection DHT11 ===")
print("Recherche du capteur sur différents GPIO...\n")

for nom, pin in gpios_a_tester:
    print(f"Test GPIO {nom}... ", end="", flush=True)
    try:
        dht = adafruit_dht.DHT11(pin)
        temperature = dht.temperature
        humidite = dht.humidity
        print(f"✓ TROUVÉ! {temperature}°C - {humidite}%")
        dht.exit()
        print(f"\n*** Le capteur est sur GPIO {nom} ***")
        print(f"Utilisez: dht = adafruit_dht.DHT11(board.{nom})")
        break
    except Exception as e:
        print(f"✗ Non détecté")
        try:
            dht.exit()
        except:
            pass
    
    time.sleep(0.5)
else:
    print("\n⚠️  Capteur non trouvé sur aucun GPIO testé")
    print("\nVérifications à faire:")
    print("1. Vérifiez le branchement (VCC, DATA, GND)")
    print("2. Essayez avec sudo: sudo python test1.py")
    print("3. Vérifiez que le capteur est bien un DHT11 (pas DHT22)")
