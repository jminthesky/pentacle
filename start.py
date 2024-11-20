import RPi.GPIO as GPIO
import time
import os
import subprocess
from mfrc522 import SimpleMFRC522




def lire_texte(texte, fichier_sortie="output.wav"):
    try:
        # Commande pour générer le fichier audio
        commande_pico = f'pico2wave -l fr-FR -w {fichier_sortie} "{texte}"'
        os.system(commande_pico)
        
        # Lecture du fichier généré
        subprocess.run(["aplay", fichier_sortie])
        
        # Optionnel : supprimer le fichier audio après lecture
        os.remove(fichier_sortie)
    except Exception as e:
        print(f"Erreur : {e}")

# Initialisation des pins GPIO et du lecteur RFID
#GPIO.setmode(GPIO.BCM)
reader = SimpleMFRC522()


try:
    while True :
      #print("Approchez votre carte RFID du lecteur")
      #id, text = reader.read()
      id = reader.read_id()
      print(f"ID de la carte: |{id}|")
      print(f"")

      if str(id) == "584197378814":
        lire_texte("Salut Robin! Comment ça va?")
      if str(id) == "138270518058":
        lire_texte("Salut Alban! Comment ça va?...")
      if str(id) == "783538561520":
        lire_texte("Salut Jean-Mi! Comment ça va?")
      time.sleep(1)
except KeyboardInterrupt:
    print("Opération interrompue.")
finally:
    GPIO.cleanup()


