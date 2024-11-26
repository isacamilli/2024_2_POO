import json

class Cliente:
    def __init__(self,id,nome,email,num):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__num = num

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__num}"
    
    #@staticmethod
    def get_idClient(self) :
        return self.__id
    
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
            if x.id > id :
                id = x.id

        obj.id = id + 1

        cls.objetos.append(obj)
        cls.salvar()

    def listar(cls):
        