janela = ['0']*24
corredor = ['0']*24
print('='*30)
print("Passagens de onibus Foguete")
print('='*30)
while True:
    menu = int(input("\n----- O que deseja? ----- "
      "\n1- Comprar passagem"
      "\n2- Cancelar compra"
      "\n3- Mostrar mapa de ocupação"
      "\n4- Sair"
      "\n-->"))

    if menu < 1 or menu > 4:
        print("Opção inválida. digite novamente")
        continue
    elif menu == 1:
        if '0' not in janela and '0' not in corredor:
            print("O ônibus está lotado, sinto muito.\n")
            continue
        opcao = int(input("Você deseja um assento na janela ou corredor?"
                       "\n1- Janela"
                       "\n2- Corredor"
                       "\n-->"))
        if opcao < 1 or opcao > 2:
            print("Opção inválida, tente novamente.")
            continue
        poltrona = int(input("Escolha uma poltrona de 1 a 24: "))
        if poltrona < 1 or poltrona > 24:
            print("Opção inválida, tente novamente.")
            continue
        elif opcao == 1 and janela[poltrona-1] == '0':
            print("Venda realizada com sucesso!")
            del janela[poltrona-1]
            janela.insert(poltrona-1, '1')
        elif opcao == 1 and janela[poltrona-1] == '1':
            print('Poltrona ocupada. Venda não realizada!')
        elif opcao == 2 and corredor[poltrona-1] == '0':
            print("Venda realizada com sucesso!")
            del corredor[poltrona - 1]
            corredor.insert(poltrona-1, '1')
        elif opcao == 2 and corredor[poltrona-1] == '1':
            print('Poltrona ocupada. Venda não realizada!')

    elif menu == 2:
        if '1' not in janela or '1' not in corredor:
            print("O ônibus está vazio, não é possivel cancelar uma passagem.")
            continue
        opcao = int(input("O assento se localiza no corredor ou na janela?"
                      "\n1- janela"
                      "\n2- corredor"
                      "\n-->"))
        if opcao < 1 or opcao > 2:
            print("Informação inválida, digite novamente.")
            continue
        poltrona = int(input("Digite o numero da poltrona: "))
        if poltrona < 1 or poltrona > 24:
            print("Informação inválida, digite novamente.")
            continue
        elif opcao == 1 and janela[poltrona-1] == '1':
            del janela[poltrona-1]
            janela.insert(poltrona-1, '0')
            print("Compra cancelada com sucesso!")
        elif opcao == 1 and janela[poltrona-1] == '0':
            print("A poltrona selecionada já está livre, compra não cancelada!")
        elif opcao == 2 and corredor[poltrona-1] == '1':
            del corredor[poltrona-1]
            corredor.insert(poltrona-1, '0')
            print("Compra cancelada com sucesso!")
        elif opcao == 2 and corredor[poltrona-1] == '0':
            print("A poltrona selecionada já está livre, compra não cancelada!")

    elif menu == 3:
        print('---Janela---')
        for a in range(len(janela)):
            if janela[a] == '0':
                print(a+1, 'Livre')
            elif janela[a] == '1':
                print(a+1, 'Ocupada')

        print("---Corredor---")
        for b in range(len(janela)):
            if corredor[b] == '0':
                print(b+1, 'Livre')
            elif corredor[b] == '1':
                print(b+1, 'Ocupada')
    elif menu == 4:
        print("Volte sempre!")
        break
