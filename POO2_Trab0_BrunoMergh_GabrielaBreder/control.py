from cadastro import Cadastro
from relatorio import Relatorio

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
                self.__lstcliente.append(cad.cadastraPessoa())
            elif opcao2 == 2:
                self.__lstfornecedor.append(cad.cadastraFornecedor())
            elif opcao2 == 3:
                self.__lstproduto.append(cad.cadastraProduto())
            elif opcao2 == 4:
                self.__lstvenda.append(cad.cadastraVenda())
            elif opcao2 == 5:
                self.__lstcompra.append(cad.cadastraCompra())
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
