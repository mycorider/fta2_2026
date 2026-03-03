import random

# Function liefert eine gültige hexadezimale Stelle zurück
def getHexZiffer():
    
    # Bestimme eine zufällige Dezimalzahl im Bereich von 0 bis 15
    ziffer = random.randint(0,15)

    # Wenn die Zahl kleiner als 10 ist liefere sie als String zurück
    if ziffer < 10:
        return str(ziffer)
    
    # Ansonsten addiere sie zu 55 und hole das entsprechende ASCII-Zeichen
    # Bsp. (55+10 = 65) --> 65 -- 'A'
    # Kopiere das Zeichen an den Aufrufer zurück
    return chr(55 + ziffer)

def getHexpaar():
    # Wir hängen zwei hexadezimale Stellen aneinander
    return getHexZiffer() + getHexZiffer()

def getMacAdress():
    # hole den ersten Block
    mac = getHexpaar()

    # schreibe 5x : + block dahinter
    for i in range(5):
        mac = mac + ":" + getHexpaar()

    # kopiere die konstruierte MAC-Adresse an den Aufrufer zurück
    return mac


### Hauptprogramm

print(getMacAdress())

