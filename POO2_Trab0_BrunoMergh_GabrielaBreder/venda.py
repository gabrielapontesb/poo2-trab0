class Venda:


    def __init__(self, cliente, dt, prod, qtd):
        self.__cliente = cliente
        self.__dt = dt
        self.__prod = prod
        self.__qtd = qtd
        
    def getCliente(self):
        return self.__cliente
    
    def setCliente(self, cliente):
        self.__cliente = cliente
        
    def getDt(self):
        return self.__dt
        
    def setDt(self):
        self.__dt = dt

    def getProd(self):
        return self.__prod

    def setProd(self, prod):
        self.__prod = prod

    def getQtd(self):
        return self.__qtd

    def setQtd(self, qtd):
        self.__qtd = qtd


