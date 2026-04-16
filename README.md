# Configuration DHT11 - Température et Humidité

Ce projet permet de lire la température et l'humidité avec un capteur DHT11 sur Raspberry Pi.

## 📦 Matériel nécessaire

- Raspberry Pi (tous modèles avec GPIO)
- Capteur DHT11
- 3 câbles jumper femelle-femelle
- Résistance 10kΩ (recommandée mais souvent déjà incluse sur les modules DHT11)

## 🔌 Branchement du DHT11

```
DHT11          Raspberry Pi
-----          ------------
VCC   ------>  Pin 1 (3.3V) ou Pin 2 (5V)
DATA  ------>  Pin 7 (GPIO 4) - configurable
GND   ------>  Pin 6 (GND)
```

**Note:** Vous pouvez utiliser un autre GPIO en modifiant `DHT_PIN` dans les scripts.

### Schéma des GPIO Raspberry Pi (vue de dessus)

```
3.3V  [ 1] [ 2]  5V
GPIO2 [ 3] [ 4]  5V
GPIO3 [ 5] [ 6]  GND
GPIO4 [ 7] [ 8]  GPIO14
GND   [ 9] [10]  GPIO15
...
```

## 🚀 Installation

### 1. Cloner ou copier les fichiers

Copiez tous les fichiers dans un dossier sur votre Raspberry Pi.

### 2. Exécuter le script d'installation

```bash
chmod +x install_dht11.sh
./install_dht11.sh
```

### 3. Activer l'environnement virtuel

```bash
source dht11_env/bin/activate
```

## 📝 Utilisation

### Script simple (lecture en continu)

```bash
python dht11_reader.py
```

Affiche la température et l'humidité toutes les 2 secondes.

### Script avancé (enregistrement CSV)

```bash
python dht11_logger.py
```

Enregistre les données dans `dht11_data.csv` avec horodatage.

### Arrêter les scripts

Appuyez sur `Ctrl+C` pour arrêter proprement.

## ⚙️ Configuration

### Changer le pin GPIO

Dans les fichiers Python, modifiez la ligne :

```python
DHT_PIN = board.D4  # GPIO 4
```

Remplacez `D4` par le GPIO que vous utilisez :
- `board.D17` pour GPIO 17 (Pin 11)
- `board.D18` pour GPIO 18 (Pin 12)
- `board.D27` pour GPIO 27 (Pin 13)
- etc.

### Changer l'intervalle de lecture

Dans `dht11_logger.py`, modifiez :

```python
INTERVAL = 2  # secondes
```

**Note:** Le DHT11 ne peut être lu que toutes les 2 secondes minimum.

## 🔧 Dépannage

### Erreur "RuntimeError: DHT sensor not found"

- Vérifiez le branchement
- Vérifiez que le bon GPIO est spécifié
- Essayez avec 5V au lieu de 3.3V pour VCC

### Erreur "RuntimeError: A full buffer was not returned"

- C'est normal, le DHT11 rate parfois des lectures
- Le script ignore ces erreurs et réessaye

### Permission refusée sur les GPIO

```bash
sudo usermod -a -G gpio $USER
# Puis déconnectez-vous et reconnectez-vous
```

Ou exécutez avec sudo :
```bash
sudo python dht11_reader.py
```

### Problèmes d'installation de pip

Si vous avez des erreurs avec pip, essayez :

```bash
pip install --upgrade pip setuptools wheel
pip install adafruit-circuitpython-dht --no-cache-dir
```

## 📊 Format des données CSV

Le fichier `dht11_data.csv` contient :

```csv
Date,Heure,Température (°C),Humidité (%)
2026-02-13,14:30:15,22.0,45.0
2026-02-13,14:30:17,22.0,45.0
```

## 📚 Documentation

- [Adafruit DHT CircuitPython](https://github.com/adafruit/Adafruit_CircuitPython_DHT)
- [Datasheet DHT11](https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf)

## 🎯 Caractéristiques du DHT11

- **Plage de température:** 0-50°C (±2°C)
- **Plage d'humidité:** 20-90% (±5%)
- **Fréquence de lecture:** 1 Hz (1 lecture/seconde max)
- **Alimentation:** 3.3V à 5V
- **Courant:** 0.3mA (mesure) / 60μA (veille)
