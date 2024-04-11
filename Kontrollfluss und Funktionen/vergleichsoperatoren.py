a = 5
b = 10
c = 15

print(a == b) # Gleichheitsoperator -> False

print(a != b) # Ungleichheitsoperator -> True

print(a > b) # Größer-als-Operator -> False
print(a < b) # Kleiner-als-Operator -> True

print(a <= b) # Kleiner-gleich-Operator -> True
print(a >= b) # Größer-gleich-Operator -> False

if a < b and b > c:
    print("B ist größer als A und C")