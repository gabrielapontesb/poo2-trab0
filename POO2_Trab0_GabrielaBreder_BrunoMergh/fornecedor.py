class Fornecedor:

    def __init__(self, nome, end, tel, cod, cnpj):
        self.__nome = nome
        self.__end = end
        self.__tel = tel
        self.__cod = cod
        self.__cnpj = cnpj


    def getNome(self):
            return self.__nome

    def setNome(self, nome):
            self.__nome = nome

    def getEnd(self):
            return self.__end

    def setEnd(self, end):
            self.__end = end

    def getTel(self):
            return self.__tel

    def setTel(self, tel):
            self.__tel = tel

    def getCod(self):
            return self.__cod

    def setCod(self, cod):
            self.__cod = cod

    def getCnpj(self):
            return self.__cnpj

    def setCnpj(self, cnpj):
            self.__cnpj = cnpj
