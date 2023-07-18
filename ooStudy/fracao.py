

# atributos
# 1. numerador; 2. denominador

# metodos
# somar; subtrair; multiplicar; dividir; inverter; inverter sinal; simplificar

class Fraction:

    def __init__(self, numerator, denominator):
        self._numerator = numerator
        if denominator == 0:
            self._denominator = 1
        else:
            self._denominator = denominator

    def sum(self, fraction):
        if self._denominator == fraction._denominator:
            num = self._numerator + fraction._numerator
            den = self._denominator
            return Fraction(num, den)
        num = self._numerator * fraction._denominator + fraction._numerator * self._denominator
        den = self._denominator * fraction._denominator
        return Fraction(num, den)
    
    def subtract(self, fraction):
        return self.sum(fraction.reverseSignal())

    def multiply(self, fraction):
        num = self._numerator * fraction._numerator
        den = self._denominator * fraction._denominator
        return Fraction(num, den)
    
    def divide(self, fraction):
        return self.multiply(fraction.reverse())

    def reverse(self):
        return Fraction(self._denominator, self._numerator)

    def reverseSignal(self):
        return Fraction(-self._numerator, self._denominator)
    
    def simplify(self):
        pass

    def __str__(self):
        representation = "{}/{}".format(self._numerator, self._denominator)
        return representation

    def __repr__(self):
        representation = "Fraction({}, {})".format(self._numerator, self._denominator)
        return representation
