n = int(input(" Son kriting: "))

s = 0
while n != 0:
    s += n % 10
    n //= 10
print(s) 