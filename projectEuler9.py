import math

for a in range(1,1000):
    for b in range(1,1000):
        cPow = a ** 2 + b ** 2
        c = math.sqrt(cPow)
        if a + b + c == 1000:
            print(a * b * c)
        
    