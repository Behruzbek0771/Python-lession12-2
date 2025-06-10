matn = input("Matn kiriting: ")
unlilar = "aeiouAEIOU" 
soni = 0

for harf in matn:
    if harf in unlilar:
        soni += 1

print(f"Unli harflar soni: {soni}")
