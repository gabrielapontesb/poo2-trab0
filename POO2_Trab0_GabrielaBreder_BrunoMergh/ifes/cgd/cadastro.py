from ifes.cdp.pessoa import Pessoa
from ifes.cdp.pfisica import Pfisica
from ifes.cdp.pjuridica import Pjuridica
from ifes.cdp.produto import Produto
from ifes.cdp.venda import Venda
from ifes.cdp.fornecedor import Fornecedor
from ifes.cdp.compra import Compra
import os

class Cadastro:

    def PopularBancoCliente(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/cliente.txt")
        lstCliente = []
        arqC = open(FILENAME, 'r')
        conteudo = arqC.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(";")
            cod = int(lstconteudo[0])
            nome = lstconteudo[1]
            tel = int(lstconteudo[2])
            end = lstconteudo[3]
            tipo = lstconteudo[4]
            if (tipo.upper() == "F"):
                cpf = int(lstconteudo[5])
                pf = Pfisica(cod, nome, tel, end, cpf)
                lstCliente.append(pf)
            elif (tipo.upper() == "J"):
                cnpj = lstconteudo[5]
                pj = Pfisica(cod, nome, tel, end, cnpj)
                lstCliente.append(pj)
            conteudo = arqC.readline()
        return lstCliente

    def PopularBancoProduto(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/produto.txt")
        lstProduto = []
        arqP = open(FILENAME, 'r')
        conteudo = arqP.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(';')
            cod = int(lstconteudo[0])
            desc = lstconteudo[1]
            estmin = int(lstconteudo[2])
            qtdatual = int(lstconteudo[3])
            custo = float(lstconteudo[4])
            pctlucro = float(lstconteudo[5])
            p = Produto(cod, desc, estmin, qtdatual, custo, pctlucro)
            lstProduto.append(p)
            conteudo = arqP.readline()
        return lstProduto

    def PopularBancoFornecedor(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/fornecedor.txt")
        lstFornecedor = []
        arqF = open(FILENAME, 'r')
        conteudo = arqF.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(';')
            nome = lstconteudo[0]
            end = lstconteudo[1]
            tel = int(lstconteudo[2])
            cod = int(lstconteudo[3])
            cnpj = lstconteudo[4]
            f = Fornecedor(nome, end, tel, cod, cnpj)
            lstFornecedor.append(f)
            conteudo = arqF.readline()
        return lstFornecedor

    def PopularBancoVenda(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/venda.txt")
        lstVenda = []
        arqV = open(FILENAME, 'r')
        conteudo = arqV.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(';')
            cliente = int(lstconteudo[0])
            data = lstconteudo[1]
            produto = int(lstconteudo[2])
            qtd = int(lstconteudo[3])
            v = Venda(cliente, data, produto, qtd)
            lstVenda.append(v)
            conteudo = arqV.readline()
        return lstVenda

    def PopularBancoCompra(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/compra.txt")
        lstCompra = []
        arqC = open(FILENAME, 'r')
        conteudo = arqC.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(';')
            qtd = int(lstconteudo[0])
            notafiscal = lstconteudo[1]
            codfornec = int(lstconteudo[2])
            codprod = int(lstconteudo[3])
            dtcompra = lstconteudo[4]
            c = Compra(qtd, notafiscal, codfornec, codprod, dtcompra)
            lstCompra.append(c)
            conteudo = arqC.readline()
        return lstCompra

    def cadastraPessoa(self):

        cod = int(input("Codigo: "))
        nome = input("Nome: ")

        tel = int(input("Telefone: "))
        end = input("Endereco: ")
        tipo = input("F para fisica e J para juridica: ")

        if (tipo.upper() == "F"):
            cpf = int(input("CPF: "))
            pf = Pfisica(cod, nome, tel, end, cpf)
        elif (tipo.upper() == "J"):
            cnpj = int(input("CNPJ: "))
            pj = Pfisica(cod, nome, tel, end, cnpj)
        else:
            print("letra incorreta")

        if (tipo.upper() == "F"):
            return pf
        elif (tipo.upper() == "J"):
            return pj
        else:
            return 0


    def cadastraProduto(self):

        cod = int(input("Codigo: "))
        desc = input("Descricao: ")
        estmin = int(input("Estoque minimo: "))
        qtdatual = int(input("Qtd atual: "))
        custo = float(input("Custo: "))
        pctlucro = int(input("Pct lucro: "))
        p = Produto(cod, desc, estmin, qtdatual, custo, pctlucro)
        return p

    def cadastraFornecedor(self):
        nome = input("Nome do fornecedor: ")
        end = input("Endereco: ")
        tel = int(input("Telefone: "))
        cod = int(input("Codigo: "))
        cnpj = int(input("Cnpj: "))
        f = Fornecedor(nome, end, tel, cod, cnpj)
        return f

    def cadastraVenda(self):
        cliente = int(input("Codigo do cliente: "))
        dt = input("Data: ")
        prod = int(input("Codigo do produto: "))
        qtd = int(input("Quantidade: "))
        v = Venda(cliente, dt, prod, qtd)
        return v

    def cadastraCompra(self):
        qtd = int(input("Quantidade: "))
        notaf = int(input("Nota fiscal: "))
        codfornec = int(input("Codigo do fornecedor: "))
        codprod = int(input("Codigo do produto: "))
        dtcompra = input("Data: ")
        c = Compra(qtd, notaf, codfornec, codprod, dtcompra)
        return c
