from pessoa import Pessoa

class Pjuridica(Pessoa):

    def __init__(self, cod, nome, tel, end, cnpj):
        super(Pjuridica, self).__init__(cod, nome, tel, end)
        self.__cnpj = cnpj

    def getCnpj(self):
        return self.__cnpj

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj