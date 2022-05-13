print("Ler o total de vendas de cada vendedor de uma loja, que tem 10 vendedores.")
vendedores = []
valores = []
percentual = []
valorReceber = []
valortotal = 0
menor = 0
maior = 0

print("Informe o nome de 10 vendedores, o valor de vendas deles, e o percentual de comisão em seguida:")
for a in range(0,3):
    nome = input("Digite o nome do vendedor: ")
    vendedores.append(nome)
    vendas = float(input("{} conseguiu vender: R$".format(vendedores[a])))
    valores.append(vendas)
    comissao = float(input("O percentual de comissão de {} é: ".format(vendedores[a])))
    percentual.append(comissao)
    valorReceber.append(valores[a] * percentual[a] / 100)
    valortotal += vendas
    maior += (nome + vendas)

for b in range(0,3):
    print("\n{} Conseguiu vender: R${}"
          "\nseu percentual de comissão é de: {}%"
          "\nsua comissão final será de: R${}".format(vendedores[b], valores[b],percentual[b], valorReceber[b]))

print("O total de vendas de todos os vendedores é: R${}".format(valortotal))