class Pessoa():

    def __init__(self, cod, nome, tel, end):
        self.__cod = cod
        self.__nome = nome
        self.__tel = tel
        self.__end = end
            
    def getCod(self):
        return self.__cod

    def setCod(self, cod):
        self.__cod = cod

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getTel(self):
        return self.__tel

    def setTel(self, tel):
        self.__tel = tel

    def getEnd(self):
        return self.__end

    def setEnd(self, end):
        self.__end = end

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        self.__tipo = tipo   
