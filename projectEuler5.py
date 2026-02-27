# import math
# print(math.lcm(*range(1, 21))) // Easier Option

numbers = set()

def control(number):
    condition = 0
    for i in range(1, 21):
        if number % i == 0:
            condition+=0
        else:
            condition+=1
    if condition < 1:
        numbers.add(number)

for i in range(2520, 10000000000 ,2520):
    control(i)

print(min(numbers))