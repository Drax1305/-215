a = 200
b = 17
while True:
    a += 1
    c = a % b
    if c == 0:
        break
print("Минимальное число большее 200 и кратное 17 =", a)