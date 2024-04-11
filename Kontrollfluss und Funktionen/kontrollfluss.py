alter = 20
student = True

if alter > 18:
    if student: # wenn student == True
        print("Volljähriger Student")
    else:
        print("Volljährig, aber kein Student")

for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")

# i = 1, j = 1
# i = 1, j = 2
# i = 2, j = 1
# i = 2, j = 2
# i = 3, j = 1
# i = 3, j = 2

for i in range(5):
    if i % 2 == 0:
        for j in range(i):
            print(f"i = {i}, j = {j}")

# i = 2, j = 0
# i = 2, j = 1
# i = 4, j = 0
# i = 4, j = 1
# i = 4, j = 2
# i = 4, j = 3