alter = 20
student = True

if alter >= 18 and student:     # and
    print("Du bist ein volljähriger Student")

if alter < 13 or student:       # or
    print("Du bist entweder jünger als 13 oder Student")

if not student:                 # not
    print("Du bist kein Student")

if (alter > 18 and student) or (alter < 13):    # Kombination
    print("Bla")