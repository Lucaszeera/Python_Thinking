# print("Receba 15 numeros inteiros, verifique existencia de elementos iguais a 30, mostrando as posições na lista em que apareceram")
# print("*--"*20)
# print("Informe 15 numeros inteiros:")
# lista = []
# for a in range(0,15):
#     numero = int(input("--> "))
#     lista += str(numero)
#     if lista[a] == '30':
#         print(a)
# print(len(lista))
# print(lista)
#
# print("A quantidade de elementos com valor 30 é: {} e foram informados na ordem: {}".format())

listaNumeros = []
lista= []
for i in range (5):
    numero = int(input("Digite um numero:"))
    listaNumeros.append(numero)
    if listaNumeros[i] == 30:
        lista.append(i+1)
print(lista)