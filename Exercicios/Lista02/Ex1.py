import math
class Cerchio :
    def __init__(self) :
        self.__raio = 0
    def set_raio(self, p) :
        if p >= 0 : self.__raio = p
        else :
            raise ValueError("O raio não pode ser negativo")
    def get_raio(self) :
        return self.__raio

    def calc_area(self) :
        area = self.__raio ** 2 * math.pi
        return area

    def calc_circ(self) :
        circ = 2 * self.__raio * math.pi
        return circ

    
class UI :
    @staticmethod
    def main() :
        x = 1
        while x != 0:
            x = UI.menu()
            if x  == 1 : UI.novo_circulo()
        
    @staticmethod
    def menu() :
        print('Digite 1 para continuar e 0 para terminar o programa: ')
        return int(input())

    @staticmethod
    def novo_circulo() :
        x = Cerchio()
        x.set_raio (float(input("Informe o valor do raio desejado:")))
        print (f"Área = {x.calc_area():.2f}")
        print (f"Circunferência = {x.calc_circ():.2f}")


UI.main()