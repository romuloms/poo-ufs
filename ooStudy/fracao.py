

# atributos
# 1. numerador; 2. denominador

# metodos
# somar; subtrair; multiplicar; dividir; inverter; inverter sinal; simplificar

class Fraction:

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        if denominator == 0:
            self.__denominator = 1
        else:
            self.__denominator = denominator

    def sum(self, fraction):
        if self.__denominator == fraction.__denominator:
            num = self.__numerator + fraction.__numerator
            den = self.__denominator
            return Fraction(num, den)
        num = self.__numerator * fraction.__denominator + fraction.__numerator * self.__denominator
        den = self.__denominator * fraction.__denominator
        return Fraction(num, den)
    
    def subtract(self, fraction):
        return self.sum(fraction.reverseSignal())

    def multiply(self, fraction):
        num = self.__numerator * fraction.__numerator
        den = self.__denominator * fraction.__denominator
        return Fraction(num, den)
    
    def divide(self, fraction):
        return self.multiply(fraction.reverse())

    def reverse(self):
        return Fraction(self.__denominator, self.__numerator)

    def reverseSignal(self):
        return Fraction(-self.__numerator, self.__denominator)
    
    def calcMDC(self, n, d):
        if (n == d):
            return n
        elif (n < d):
            return self.calcMDC(d, n)
        elif (d < n):
            return self.calcMDC(n-d, d)
    
    def simplify(self):
        factor = self.calcMDC(self.__numerator, self.__denominator)
        newNum = int(self.__numerator/factor)
        newDen = int(self.__denominator/factor)
        return Fraction(newNum, newDen)
    
    def greaterEqual(self, fraction):
        firstFrac = self.__numerator / self.__denominator
        secondFrac = fraction.__numerator / fraction.__denominator

        return firstFrac >= secondFrac

    def __str__(self):
        representation = "{}/{}".format(self.__numerator, self.__denominator)
        return representation

    def __repr__(self):
        representation = "Fraction({}, {})".format(self.__numerator, self.__denominator)
        return representation
    
    def __add__(self, other):
        return self.sum(other)
    
    def __sub__(self, other):
        return self.subtract(other)
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def __ge__(self, other):
        return self.greaterEqual(other)

    def __neg__(self):
        return self.reverseSignal()
