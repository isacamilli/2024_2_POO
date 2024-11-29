from proj_venda import Venda
from proj_produto import Produto

class vendaitem:
    def __init__(self, id, qtd, preco):
        self.__id = id
        self.__qtd = qtd
        self.__preco = Produto.get_precoProduto()
        self.__idVenda = Venda.get_idVenda()
        self.__idProduto = Produto.get_idProduto()

    def __str__(self):
        return f"{self.__id} - {self.__qtd} - {self.__preco} - {self.__idVenda} - {self.__idProduto}"
    
    def get_idItem(self) :
        return self.__id
    
    def get_qtditem(self):
        return self.__qtd
    
    