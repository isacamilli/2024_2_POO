class Categoria:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
    
    def get_idCategoria(self):
        return self.__id
    
    def get_descrCategoria(self):
        return self.__descricao
    
    