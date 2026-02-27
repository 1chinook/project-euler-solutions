import math

hundredFact = math.factorial(100)

def digitFinder(number):
    return [int(d) for d in str(number)]

digits = digitFinder(hundredFact)

print(sum(digits))