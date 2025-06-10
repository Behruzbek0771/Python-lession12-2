parol = 771
urinish = 1

javob = int(input("Parol nima? "))

if javob == parol:
    print(f"Siz to'g'ri topdingiz, urinishlar soni: {urinish}")
else:
    while urinish < 3:
        urinish += 1
        javob = int(input("Yana urinib ko'ring: "))
        if javob == parol:
            print(f"Siz to'g'ri topdingiz, urinishlar soni: {urinish}")
            break
    else:
        print(f"Siz bloklandingiz, urinishlar soni: {urinish}")
