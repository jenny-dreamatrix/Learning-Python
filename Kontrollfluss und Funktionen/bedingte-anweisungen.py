alter = 20

if alter < 13:
    print("Du bist ein Kind")
elif alter < 18:
    print("Du bist ein Jugendlicher")
else:
    print("Du bist volljährig")

alter2 = 18
hat_führerschein = True

if alter2 >= 18:
    if hat_führerschein:
        print("Du darfst Auto fahren")
    else:
        print("Du bist volljährig, aber darfst kein Auto fahren")
else:
    print("Du bist nicht volljährig")