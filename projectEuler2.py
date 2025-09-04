a=1
b=2
c = 0
fibonacciNums = []
fibonacciEvenNums = []

while c < 4000000:
    c = a + b
    a = b
    b = c
    fibonacciNums.append(a)


for i in fibonacciNums:
    if i % 2 == 0:
        fibonacciEvenNums.append(i)


sumOfEvenNumbers = sum(fibonacciEvenNums)
print(sumOfEvenNumbers)