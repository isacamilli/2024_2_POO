import randint from random

class Bingo :
    def __init__(self,numBolas,bolas) :
        self.__numBolas = numBolas
        self.__bolas = bolas
    def __str__(self) :
        return self.__bolas


class UI :
    @staticmethod
    def menu() :
        print ("Quer começar um novo jogo?")
        print("1 - Sim, 0 - Não")
        return int(input())

    @staticmethod
    def main() :
        op = 1
        jogo = None
        contador = 0
        sort = []
        while op == 1 :
            op = UI.menu()
            if op == 1 :
                jogo = UI.novo_jogo()
            
            while contador != num_b :
                randint


    @staticmethod
    def novo_jogo() :
        num_b = int(input("Insira a quantidade de bolas dessa rodada: "))
        tuas_bolas = list(map(int,input("Insira os números sorteados por você: ").split()))
        jogoCriado = Bingo(num_b,tuas_bolas)
    
    