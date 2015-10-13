class Compra:

	def __init__(self, qtd, notaf, codfornec, codprod, dtcompra):
		self.__qtd = qtd
		self.__notaf = notaf
		self.__codfornec = codfornec
		self.__codprod = codprod
		self.__dtcompra = dtcompra

	def getQtd(self):
		return self.__qtd

	def setQtd(self, qtd):
		self.__qtd = qtd

	def getNotaf(self):
		return self.__notaf

	def setNotaf(self, notaf):
		self.__notaf = notaf

	def getCodfornec(self):
		return self.__codfornec

	def setCodfornec(self, codfornec):
		self.__codfornec = codfornec

	def getCodprod(self):
		return self.__codprod

	def setCodprod(self, codprod):
		self.__codprod = codprod

	def getDtcompra(self):
		return self.__dtcompra

	def setDtcompra(self, dtcompra):
		self.__dtcompra = dtcompra