from control import Control

class Menu():



    def imprimirMenu(self):
        ctrl = Control()
        print("\n" * 10)
        print("Gerenciamento da Padaria Otarios\n")
        print("Deseja fazer upload do banco de dados?\n")
        print("1 - SIM ")
        print("2 - NAO \n")
        resp = int(input("Escolha a opcao desejada: "))
        if resp == 1:
            ctrl.Controle(3, 0)
            print("\nUPDATE DO BANCO GERADO COM SUCESSO\n")

        print("\n" *2)
        print("Gerenciamento da Padaria Otarios\n")
        print("1 - Cadastrar")
        print("2 - Relatorios")
        print("3 - Sair\n")
        opcao = int(input("Digite a opcao desejada: "))
        operacao = 's'


        while operacao.lower() != 'n':
            if opcao == 1:
                print('\n' * 50)
                print("Gerenciamento da Padaria Otarios\n")
                print("1 - Cadastrar Cliente")
                print("2 - Cadastrar Fornecedor")
                print("3 - Cadastrar Produto")
                print("4 - Cadastrar Venda")
                print("5 - Cadastrar Compra\n")
                opcao2 = int(input("Digite a opcao desejada: "))

                if opcao2 == 1:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    print("Cadastrar Cliente\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Cliente cadastrado com sucesso\n")

                elif opcao2 == 2:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    print("Cadastrar Fornecedor\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Fornecedor cadastrado com sucesso\n")

                elif opcao2 == 3:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    print("Cadastrar Produto\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Produto cadastrado com sucesso\n")

                elif opcao2 == 4:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    print("Cadastrar Venda\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Venda cadastrada com sucesso\n")

                elif opcao2 == 5:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    print("Cadastrar Compra\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Compra cadastrada com sucesso\n")

            elif opcao == 2:
                print("\n" * 40)
                print("Gerenciamento da Padaria Otarios\n")
                print("1 - Gerar relatorio 'A pagar'")
                print("2 - Gerar relatorio 'A receber'")
                print("3 - Gerar relatorio 'Vendas e Lucro por Produto'")
                print("4 - Gerar relatorio 'Estoque Atual'")
                print("5 - Todos \n")
                opcao2 = int(input("Digite a opcao desejada: "))

                if opcao2 == 1:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Relatorio gerado com sucesso\n")

                elif opcao2 == 2:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Relatorio gerado com sucesso\n")

                elif opcao2 == 3:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Relatorio gerado com sucesso\n")

                elif opcao2 == 4:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Relatorio gerado com sucesso\n")

                elif opcao2 == 5:
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    ctrl.Controle(opcao, opcao2)
                    print("Relatorio gerado com sucesso\n")

            elif opcao == 3:
                print('\n' * 50)
                print("Programa finalizado com sucesso\n")
                break
            while True:
                operacao = input("Deseja fazer mais alguma operacao s/n? \n")
                if operacao.lower() == 's':
                    print("\n" * 40)
                    print("Gerenciamento da Padaria Otarios\n")
                    print("1 - Cadastrar")
                    print("2 - Relatorios")
                    print("3 - Sair\n")
                    opcao = int(input("Digite a opcao desejada: "))
                    break
                elif operacao.lower() == 'n':
                    print("\n" * 40)
                    print("Programa finalizado com sucesso\n")
                    break
                else:
                    print("\n" * 40)
                    print("Letra errada, digite novamente S para nova operacao e N para sair\n")

