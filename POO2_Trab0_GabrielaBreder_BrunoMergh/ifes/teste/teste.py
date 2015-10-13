import unittest

from ifes.cdp.pessoa import Pessoa
from ifes.cdp.produto import Produto
from ifes.cdp.fornecedor import Fornecedor
from ifes.cdp.compra import Compra
from ifes.cdp.venda import  Venda


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa = Pessoa("0", "Bruno", 27997743714, "Rua qualquer")
        self.produto = Produto(0,"miojo",3,5,3.2,40)
        self.fornecedor = Fornecedor("Casas Bahia","Rua 1", 999, 0, 122)
        self.compra = Compra(1,111,0,0,"12/01/2015")
        self.venda = Venda(0,"13/01/2015",0,1)

    def testAtributosPessoa(self):
        self.assertEqual(self.pessoa.getCod(), "0")
        self.assertEqual(self.pessoa.getNome(), "Bruno")
        self.assertEqual(self.pessoa.getTel(), 27997743714)
        self.assertEqual(self.pessoa.getEnd(), "Rua qualquer")

    def testAtributosProduto(self):
        self.assertEqual(self.produto.getCod(), 0)
        self.assertEqual(self.produto.getDesc(), "miojo")
        self.assertEqual(self.produto.getEstmin(), 3)
        self.assertEqual(self.produto.getQtdatual(), 5)
        self.assertEqual(self.produto.getCusto(), 3.2)
        self.assertEqual(self.produto.getPctlucro(), 40)

    def testAtributosFornecedor(self):
         self.assertEqual(self.fornecedor.getNome(), "Casas Bahia")
         self.assertEqual(self.fornecedor.getEnd(), "Rua 1")
         self.assertEqual(self.fornecedor.getTel(), 999)
         self.assertEqual(self.fornecedor.getCod(), 0)
         self.assertEqual(self.fornecedor.getCnpj(), 122)

    def testAtributosCompra(self):
        self.assertEqual(self.compra.getQtd(), 1)
        self.assertEqual(self.compra.getNotaf(), 111)
        self.assertEqual(self.compra.getCodfornec(), 0)
        self.assertEqual(self.compra.getCodprod(), 0)
        self.assertEqual(self.compra.getDtcompra(), "12/01/2015")

    def testAtributosVenda(self):
        self.assertEqual(self.venda.getCliente(), 0)
        self.assertEqual(self.venda.getDt(), "13/01/2015")
        self.assertEqual(self.venda.getProd(), 0)
        self.assertEqual(self.venda.getQtd(), 1)

    #def testApagar(self):
        #self, lstFornec, lstProd, lstComp
        #arquivo.write("Fornecedor;quantia a pagar\n")



if __name__ == "__main__":
    unittest.main()
