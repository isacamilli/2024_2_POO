class Retangulo :
    def __init__(self,b,h) :
        # if b > 0 : __b = b 
        # if h > 0 : __h = h 
        self.set_base(b)
        self.set_altura(h)

        def set_base(self,v) :
            if v > 0 : __b = v
            else: raise ValueError("a base do retângulo não pode ser negativa")
        def set_altura(self,v) :
            if v > 0 : __h = v
            else: raise ValueError("a altura do retângulo não pode ser negativa")

        def get_base(self) :
            return self.__b
        def get_altura(self) :
            return self.__h

        def CalcArea(self) :
            area = self.__b * self.__h
            return area