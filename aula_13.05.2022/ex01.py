print("Digite 7 valores e calcule os multiplos de 2 e de 3")
mult2 = 0
mult3 = 0
lista1 = []
lista2 = []
for a in range (0,7):
    valor = int(input("Digite um valor inteiro: "))
    if valor % 2 == 0:
        mult2 += 1
        lista1 += str(valor)
    elif valor % 3 == 0:
        mult3 += 1
        lista2 += str(valor)
print("fim")
print("Desses 7 numeros, {} são multiplos de 2. eles são: {}".format(mult2, lista1))
print("Desses 7 numeros, {} são multiplos de 3. eles são: {}".format(mult3, lista2))
