from fracao import Fraction


fractionA = Fraction(8, 4)
fractionB = Fraction(1, 5)

# sumFirstSecond = firstFraction.sum(secondFraction)

# mult = secondFraction.multiply(firstFraction)

# rev = firstFraction.reverse()
# list = [2, 'LUL', firstFraction]
# print(sumFirstSecond)

add = fractionA + fractionB
sub = fractionA - fractionB
neg = -fractionA
simpl = fractionA.simplify()

# print(add)
# print(sub)
# print(neg)
print(simpl)