#!/bin/bash

# Script d'installation pour DHT11
echo "=== Installation du capteur DHT11 ==="

# Créer l'environnement virtuel
echo "Création de l'environnement virtuel..."
python3 -m venv dht11_env

# Activer l'environnement virtuel
echo "Activation de l'environnement virtuel..."
source dht11_env/bin/activate

# Installer les dépendances
echo "Installation des librairies Adafruit..."
pip install --upgrade pip
pip install adafruit-circuitpython-dht
pip install adafruit-blinka

echo ""
echo "=== Installation terminée! ==="
echo ""
echo "Pour activer l'environnement virtuel :"
echo "  source dht11_env/bin/activate"
echo ""
echo "Pour lancer le script de lecture :"
echo "  python dht11_reader.py"
echo ""
