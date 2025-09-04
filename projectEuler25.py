a = 1
b = 1
fibonacciNums = [1,1]


while len(str(b)) < 1000:
    c = a + b
    a = b 
    b = c
    fibonacciNums.append(b)

lastIndex = fibonacciNums.index(fibonacciNums[-1])

print(lastIndex + 1) 
