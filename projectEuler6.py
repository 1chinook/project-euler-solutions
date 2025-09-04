
squareOfSum = []

sumOf = 0

for i in range(0,101):
    sumOf += pow(i, 2)
    squareOfSum.append(i)
    
lastRemainder = pow(sum(squareOfSum), 2) - sumOf
print(lastRemainder)