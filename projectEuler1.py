numbers = []

for i in range(3,1000):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)


sumOfNumbers = sum(numbers)

print(sumOfNumbers)