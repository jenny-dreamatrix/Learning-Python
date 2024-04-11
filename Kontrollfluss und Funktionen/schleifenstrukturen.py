zahlen = [1, 2, 3, 4, 5]

# for in loop benutzen wir, wenn wir wissen WIE OFT wir die schleife ausführen wollen
for zahl in zahlen:
    print(zahl)

# while loop wird so lange durchgeführt so lange eine bestimmte bedingung True ist
# das verwenden wir z.b., wenn wir nicht genau wissen wie oft geloopt werden soll

i = 1
while i <=5:
    print(i)
    i += 1

for zahl in zahlen:
    if zahl == 3:
        continue # 3 wird übersprungen
    print(zahl)
    if zahl == 4:
        break # bei 4 wird aufgehört
# 1, 2, 4


for i in range(1, 3):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")