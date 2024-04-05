
class Reta():
    def __init__(self, a, b):
        self.__a = a  # __ para privar alguma função para o usuário
        self.__b = b

    def setA(self, a):  # função para controlar os valores que podem entrar na função
        if (a > 0):
            self.__a = a
        else:
            self.__a = 0

    def setB(self, b):
        if (b > 0):
            self.__b = b
        else:
            self.__b = 0

    def interpolar(self, x):
        y = self.__a * x + self.__b
        return y

    def model(self):
        print(f'Os parâmetros do meu modelo de reta são: a={self.a}, b={self.b}')


import math
class Circle():
    def __init__(self, r, xo=0, yo=0):
        self.r = r
        self.xo = xo
        self.yo = yo

    def equacao_reduzida(self, xi, yi):
        return math.sqrt((xi - self.xo)**2 + (yi - self.yo)**2)

    def circunferencia(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r**2

    def model(self):
        print(f'Os parâmetros do meu modelo de círculo são: c={self.circunferencia()}, e={self.area()}, r={self.r}')

