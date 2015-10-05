class Produto:

    def __init__(self,cod, desc, estmin, qtdatual, custo, pctlucro):
        self.__cod = cod
        self.__desc = desc
        self.__estmin = estmin
        self.__qtdatual = qtdatual
        self.__custo = custo
        self.__pctlucro = pctlucro

    def getCod(self):
        return self.__cod

    def setCod(self, cod):
        self.__cod = cod

    def getDesc(self):
        return self.__desc

    def setDesc(self, desc):
        self.__desc = desc

    def getEstmin(self):
        return self.__estmin

    def setEstmin(self, estmin):
        self.__estmin = estmin

    def getQtdatual(self):
        return self.__qtdatual

    def setQtdatual(self, qtdatual):
        self.__qtdatual = qtdatual

    def getCusto(self):
        return self.__custo

    def setCusto(self, custo):
        self.__custo = custo

    def getPctlucro(self):
        return self.__pctlucro

    def setPctlucro(self, pctlucro):
        self.__pctlucro = pctlucro