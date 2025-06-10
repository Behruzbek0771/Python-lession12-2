matn = input("Matn kiriting: ")
soni = 0

for harf in matn:
    if harf.isupper():
        soni += 1

print(f"Katta harflar soni: {soni}")

