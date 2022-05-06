count = 1
tabuada = 1
while tabuada < 11:
    print(count, "*", tabuada , "=", count * tabuada)
    tabuada += 1
    if tabuada == 11:
        count += 1
        tabuada = 1
    if count == 11:
        break
print("Fim")