class cerchio :
    p = 3.14
    def __init__(self) :
        self.r = 0
    def area(self) :
        # p = 3.14
        area = self.r**2 * self.p
        return area
    def circunferencia(self) :
        circ = 2 * self.p * self.r 
        return circ

a = cerchio()
a.r = int(input("Informar valor do raio: ))
print (a.area(), a.circunferencia())
