class Relatorio:

    def apagar(self, lstFornec, lstProd, lstComp):
        #valor devido aos fornecedores
        arquivo = open('WriteApagar.txt', 'w')
        arquivo.write("Fornecedor;quantia a pagar\n")
        total = 0
        for i in range(len(lstFornec)):
            for j in range(len(lstComp)):
                if (lstFornec[i].getCod() == lstComp[j].getCodfornec()):
                    for k in range(len(lstProd)):
                        if(lstComp[j].getCodprod() == lstProd[k].getCod()):
                            valor = lstProd[k].getCusto() * lstComp[j].getQtd()
                            break

                    total += valor
                    valor = 0

            arquivo.write(str(lstFornec[i].getCod()) + ";" + str(round(total,2)) + "\n")
            total = 0

    def areceber(self, lstPessoa, lstVendas, lstProd):
        #valor total de vendas
        arquivo = open('WriteAreceber.txt', 'w')
        arquivo.write("Cliente;quantia a receber\n")
        total = 0
        for i in range(len(lstPessoa)):
            total = 0
            for j in range(len(lstVendas)):
                if (lstPessoa[i].getCod() == lstVendas[j].getCliente()):
                    for k in range(len(lstProd)):
                        if (lstVendas[j].getProd() == lstProd[k].getCod()):
                            valor = (((lstProd[k].getPctlucro()/100) * lstProd[k].getCusto()) + lstProd[k].getCusto()) * lstVendas[j].getQtd()
                            break
                    total += valor
                    valor = 0
            arquivo.write(str(lstPessoa[i].getNome()) + ";" + str(round(total,2)) + "\n")

    def vendasprod(self, lstProd, lstVendas):
        #vendas e lucro por produto
        arquivo = open('WriteVendasPorProduto.txt', 'w')
        arquivo.write("Descricao do Produto;Total de venda bruta;Total de lucro \n")
        total= totalp = 0
        for i in range(len(lstProd)):
            for j in range(len(lstVendas)):
                if (lstProd[i].getCod() == lstVendas[j].getProd()):

                    valor = (((lstProd[i].getPctlucro()/100) * lstProd[i].getCusto()) + lstProd[i].getCusto()) * lstVendas[j].getQtd()
                    perc = ((lstProd[i].getPctlucro()/100) * lstProd[i].getCusto()) * lstVendas[j].getQtd()

                total += valor
                totalp += perc
                valor = 0
                perc = 0
            arquivo.write(str(lstProd[i].getDesc()) + ";" + str(round(total, 2)) + ";" + str(round(totalp, 2)) + "\n")
            total = totalp = 0

    def estoque(self, lstProd, lstVendas, lstComp):

        arquivo = open('WriteEstoque.txt', 'w')
        for i in range(len(lstProd)):
            for j in range(len(lstComp)):
                if (lstProd[i].getCod() == lstComp[j].getCodprod()):
                    lstProd[i].setQtdatual(lstProd[i].getQtdatual() + lstComp[j].getQtd())

        for i in range(len(lstProd)):
            for j in range(len(lstVendas)):
                if (lstProd[i].getCod() == lstVendas[j].getProd()):
                    lstProd[i].setQtdatual(lstProd[i].getQtdatual() - lstVendas[j].getQtd())

        arquivo.write("Codigo;Descricao;Quantidade Atual; \n")
        for i in range(len(lstProd)):
            if (lstProd[i].getQtdatual() < lstProd[i].getEstmin()):
                arquivo.write(str(lstProd[i].getCod()) + ";" + str(lstProd[i].getDesc())  + ";" + str(lstProd[i].getQtdatual()) + ";COMPRAR MAIS")
                arquivo.write("\n")
            else:
                arquivo.write(str(lstProd[i].getCod()) + ";" + str(lstProd[i].getDesc())  + ";" + str(lstProd[i].getQtdatual()) +  ";")
                arquivo.write("\n")