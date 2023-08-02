import math

class Ponto:
    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        self.setX(x)
        self.setY(y)

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, newX):
        self.__x = newX

    def setY(self, newY):
        self.__y = newY

    def imprime(self):
        print("({}, {})".format(self.getX(), self.getY()))

    def distanciaPontos(self, p):
        diferencaAbs = self.__x - p.getX()
        diferencaOrd = self.__y - p.getY()
        xSqr = diferencaAbs * diferencaAbs
        ySqr = diferencaOrd * diferencaOrd
        distancia = math.sqrt(xSqr + ySqr)
        
        return distancia