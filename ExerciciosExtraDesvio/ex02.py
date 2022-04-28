num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

if num1 % num2 == 0 or num2 % num1 == 0:
    print("Os dois numeros são divisíveis!")
else:
    print("Os dois numeros não são divisiveis.")
