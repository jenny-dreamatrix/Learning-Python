# range fängt default mäßig immer bei 0 an und endet VOR der angegebenen zahl
for i in range(5): # von 0 bis 4 wird eine for schleife durchgeführt
    print(i)

for i in range(10):
    if i == 5:
        break # nach 5 wird die schleife beendet
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue # alle geraden Zahlen werden übersprungen -> alle ungeraden Zahlen werden ausgegeben
    print(i)

for i in range(1, 10, 2): # 1 ist Startpunkt, 9 ist Endpunkt, 2 ist die Schrittgröße
    print(i)

for i in range (1, 10):
    if i % 5 == 0:
        break
    if i % 2 == 0:
        continue
    print(i)