# Variable deklarieren (Wert zuweisen)
# 5 ist Datentyp integer (ganze Zahl)
# Datentyp wird automatisch erkannt, muss nicht extra zugewiesen werden, keine Typendeklaration
# der Datentyp darf sich ändern ! dynamisch !
x = 5

# Datentyp string
name = "Jenny"

a, b, c = 5, 4, "Tim"

#integer - ganze Zahlen
#float - Dezimalzahlen
#string - Text / Zeichenkette

alter = 30 #integer
gewicht = 14.5 #float
name = "Alex" #string

#globale oder lokale variablen

def meine_funktion():
    lokal = "Ich bin lokal"
    print(lokal)

# print(lokal) - nicht möglich außerhalb von der Funktion

def set_global_var():
    global global_var #so kann man eine Variable innerhalb einer Funktion global machen, mit dem keyword global
    global_var = "Global"

print(global_var)
