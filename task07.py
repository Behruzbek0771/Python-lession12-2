eng_katta = 0

for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    if eng_katta == 0 or son > eng_katta:
        eng_katta = son

print(f"Eng katta son: {eng_katta}")




