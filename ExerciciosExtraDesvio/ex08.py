opcao = int(input("Menu de opções: \n"
      "1 - Somar dois numeros\n"
      "2 - Raiz quadrada de um numero\n"
      "Digite a Opção desejada: "))
if opcao == 1:
    num1 = float(input("Digite um numero real: "))
    num2 = float(input("Digite outro numero real: "))
    print("A soma desses dois numeros é: {}".format(num1 + num2))
elif opcao == 2:
    num3 = float(input("Digite um numero real: "))
    print("A raiz quadrada desse numero é: {}".format(num3 ** 0.5))
    print("A raiz quadrada desse numero é: {}".format(pow(num3, 0.5)))
else:
    print("Opção inválida.")