from proj_categoria import Categoria

class Produto:
    def __init__(self, id, descricao, preco, estoque):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__idCategoria = Categoria.get_idCategoria

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__preco} - {self.__estoque} - {self.__idCategoria}"
    
    def get_idProduto(self):
        return self.__id
    
    def get_descricaoProduto(self):
        return self.__descricao
    
    def get_precoProduto(self):
        return self.__preco
    
    def get_estoqueProduto(self):
        return self.__estoque