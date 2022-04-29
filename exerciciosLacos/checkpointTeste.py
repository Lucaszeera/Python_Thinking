print("Bem vindo a nosso restaurante!")
pratos = int(input("Digite a quantidade de pratos principais: "))
notaFiscal = float(input("Digite o valor total da nota: R$"))
temCupom = input("Você tem cupom? Digite S ou N\n"
                 "-->")
if temCupom == 'S':
    cupom = input("Digite o cupom: ")
    if cupom == "BORALA10" or "BORALA05":
        print("Cupom aceito!")
    else:
        print("Cupom negado.")
else:
    print("Valor Inválido")
primeira = input("É a primeira vez que você vem ao restaurante? Digite S ou N\n"
                 "--.")
desconto = 0
if pratos > 3: desconto += 4

if notaFiscal > 500: desconto += 6

if cupom == "BORALA10": desconto += 10

if cupom == "BORALA05": desconto += 5







print(f"O valor original da nota é: R${notaFiscal} mas com desconto é: R$?")


