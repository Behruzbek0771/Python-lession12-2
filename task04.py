import random

sirli_son = random.randint(1, 20)

print(" Men 1 dan 20 gacha bir son o'yladim. Topishga 3 urinish bor!")

counter = 0

while True:
    taxmin = int(input("Sonni kiriting: "))
    counter += 1
    if taxmin == sirli_son:
        print(" Topdingiz!")
        break
    else:
        print(" Noto'g'ri.")