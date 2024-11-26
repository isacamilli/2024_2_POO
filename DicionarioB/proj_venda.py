from proj_cliente import Cliente

class Venda:
    def __init__(self, id, data, carrinho, total, idCliente):
        self.__id = id
        self.__data = data
        self.__carrinho = carrinho
        self.__total = total
        self.__idCliente = Cliente.get_idCliente()

    def __str__(self) :
        return f"{self.__id} - {self.__data} - {self.__carrinho} - {self.__total} - {self.__idCliente}"
    
    def get_idVenda(self) :
        return self.__id
        
    def get_data(self) :
        return self.__data
        
    def get_carrinho(self) :
        return self.__carrinho
        
    def get_total(self) :
        return self.__total
        
    def