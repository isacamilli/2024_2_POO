import json

class Cliente:
    def __init__(self,id,nome,email,num):
        self.__id = 0
        self.__nome = nome
        self.__email = email
        self.__num = num

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__num}"
    
    def get_idCliente(self) :
        return self.__id
    
    def set_id(self,id) :
        self.__id = id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self) :
        return self.__email
    
    def get_num(self) :
        return self.__num
    

class Clientes: 
    lista_clientes = []

    @classmethod
    def inserir(cls, obj) :
        cls.abrir()

        id = 0
        for x in cls.lista_clientes:
            idSet = x.get_idCliente()
            if idSet > id : id = idSet + 1

        obj.set_id(id)

        cls.lista_clientes.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.lista_clientes
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.lista_clientes :
            idSet = x.get_idCliente
            if idSet == id : return x
        return None
    
    @classmethod
    def atualizar(cls, obj) :
        idSet = obj.get_idCliente()
        x = obj.listar_id(idSet)
        if x != None:
            x.set_nome(obj.get_nome)