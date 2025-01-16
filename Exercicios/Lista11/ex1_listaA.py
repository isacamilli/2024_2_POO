from math import sqrt

class Retangulo:
    def __init__(self, base, altura):
        self.set_base(base)
        self.set_altura(altura)

    def __str__(self):
        return f"Base: {self.__base} - Altura: {self.__altura}"

    def set_base(self,base):
        if base < 0:
            raise ValueError("A base não pode ser menor ou igual a 0")
        
        else: self.__base = base

    def set_altura(self,altura):
        if altura < 0:
            raise ValueError("A altura não pode ser menor ou igual a 0")
        
        else: self.__altura = altura

    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura 
    
    def calc_area(self):
        area = self.__base * self.__altura
        return area
    
    def calc_diagonal(self):
        diagonal = sqrt(self.__base ** 2 + self.__altura ** 2)
        return diagonal
    

class Quadrado(Retangulo):
    def __init__(self, lado):
        self.set_lado(lado)

    def set_lado(self, lado):
        if lado < 0 :
            raise ValueError("O lado não pode ser menor que 0")
        
        else: self.__lado = lado

    def __str__(self):
        return f"Lado: {self.__lado}"
    
    def calc_area(self):
        area = self.__lado ** 2
        return area
    
    def calc_diagonal(self):
        diagonal = sqrt(self.__lado ** 2 * 2)
        return diagonal
    
    
    


x = Retangulo(8,9)
y = Quadrado(2)

print(x)
print(y)
print(x.calc_area())
print(y.calc_area())
print(x.calc_diagonal())
print(y.calc_diagonal())
print(type(x))
print(isinstance(x, object))
print(isinstance(x, Retangulo))
print(isinstance(x, Quadrado))
print(type(y))
print(isinstance(y, object))
print(isinstance(y, Retangulo))
print(isinstance(y, Quadrado))