def grüße(name):
    print(f"Hallo {name}")

grüße("Max")

def addiere(a, b):
    print(a + b)
    return a + b

addiere(4, 5)

def drucke_liste(meine_liste):
    for element in meine_liste:
        print(element)

def verabschiedung(name="sehr geehrte Damen und Herren"): #default Parameter angeben
    print(f"Auf Wiedersehen, {name}!")

verabschiedung()
verabschiedung("Anne")
