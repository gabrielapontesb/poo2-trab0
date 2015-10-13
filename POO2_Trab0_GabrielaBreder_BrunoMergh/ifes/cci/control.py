from ifes.cgd.cadastro import Cadastro
from ifes.cgd.relatorio import Relatorio

class Control:

    def __init__(self):
        self.__lstcliente = []
        self.__lstproduto = []
        self.__lstfornecedor = []
        self.__lstcompra =[]
        self.__lstvenda = []

    def Controle(self, opcao, opcao2):

        cad = Cadastro()
        relatorio = Relatorio()


        if opcao == 1:
            if opcao2 == 1:
                p = cad.cadastraPessoa()
                achou = False
                for cliente in range(len(self.__lstcliente)):
                    if p.getCod() == self.__lstcliente[cliente].getCod():
                        print("Cliente ja cadastrado\n")
                        achou = True
                        break
                if achou == False:
                    self.__lstcliente.append(p)
                    print("Cliente cadastrado com sucesso\n")

            elif opcao2 == 2:
                p = cad.cadastraFornecedor()
                achou = False
                for fornecedor in range(len(self.__lstfornecedor)):
                    if p.getCod() == self.__lstfornecedor[fornecedor].getCod():
                        print("Fornecedor ja cadastrado\n")
                        achou = True
                        break

                if achou == False:
                    self.__lstfornecedor.append(p)
                    print("Fornecedor cadastrado com sucesso\n")

            elif opcao2 == 3:
                p = cad.cadastraProduto()
                achou = False
                for produto in range(len(self.__lstproduto)):
                    if p.getCod() == self.__lstproduto[produto].getCod() and p.getDesc() == self.__lstproduto[produto].getDesc():
                        self.__lstproduto[produto].setQtdatual(self.__lstproduto[produto].getQtdatual() + p.getQtdatual())
                        print("Produto ja cadastrado. Qtd atual incrementada\n")
                        achou = True
                        break

                    elif p.getCod() == self.__lstproduto[produto].getCod() and p.getDesc() != self.__lstproduto[produto].getDesc():
                        print("O produto " + self.__lstproduto[produto].getDesc() + " ja utiliza esse codigo")
                        achou = True
                        break

                if achou == False:
                    self.__lstproduto.append(p)
                    print("Produto cadastrado com sucesso\n")

            elif opcao2 == 4:
                p = cad.cadastraVenda()
                self.__lstvenda.append(p)

            elif opcao2 == 5:
                p = cad.cadastraCompra()
                self.__lstcompra.append(p)

        elif opcao == 2:
            if opcao2 == 1:
                relatorio.apagar(self.__lstfornecedor, self.__lstproduto, self.__lstcompra)
            elif opcao2 == 2:
                relatorio.areceber(self.__lstcliente, self.__lstvenda, self.__lstproduto)
            elif opcao2 == 3:
                relatorio.vendasprod(self.__lstproduto, self.__lstvenda)
            elif opcao2 == 4:
                relatorio.estoque(self.__lstproduto, self.__lstvenda, self.__lstcompra)
            elif opcao2 == 5:
                relatorio.estoque(self.__lstproduto, self.__lstvenda, self.__lstcompra)
                relatorio.apagar(self.__lstfornecedor, self.__lstproduto, self.__lstcompra)
                relatorio.areceber(self.__lstcliente, self.__lstvenda, self.__lstproduto)
                relatorio.vendasprod(self.__lstproduto, self.__lstvenda)
        elif opcao == 3:
            self.__lstcliente = cad.PopularBancoCliente()
            self.__lstfornecedor = cad.PopularBancoFornecedor()
            self.__lstproduto = cad.PopularBancoProduto()
            self.__lstcompra = cad.PopularBancoCompra()
            self.__lstvenda = cad.PopularBancoVenda()

__author__ = 'Bruno'
