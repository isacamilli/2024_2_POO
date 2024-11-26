class Carrinho:
    def __init__(self, cliente, data) :
        self.__cliente = cliente
        self.__data = data
        self.__itens = []

    def __str__(self):
        return f"{self.__cliente} - {self.__data}" + f"\n".join(str(a) for a in self.__itens)
    
    def get_cliente(self):
        return self.__cliente

    def get_data(self):
        return self.__data

    def get_itens(self):
        return self.__itens

    def listar_item()

class Item:

    def __init__(self, produto, qtd, preco_unit):
        self.__produto = produto
        self.set_qtd(qtd)
        self.set_preco_unit(preco_unit)

    def __str__(self):
        return f"{self.__produto} - {self.__qtd} - {self.__preco_unit:.2f}"

    # def set_produto(self,qtd):
    #     if qtd > 0 and type(qtd) == int:
    #         self.__qtd = qtd
    #     else:
    #         raise ValueError("O elemento precisa de uma nomenclatura")

    def set_qtd(self,qtd):
        if qtd > 0 and type(qtd) == int:
            self.__qtd = qtd
        else:
            raise ValueError("O valor precisa ser inteiro e maior que zero")

    def set_preco_unit(self,preco_unit):
        if qtd > 0 and type(qtd) == int:
            self.__preco_unit = preco_unit
        else:
            raise ValueError("O valor precisa ser maior que zero")

    def total(self):
        val = self.__qtd * self.__preco_unit
        return val

