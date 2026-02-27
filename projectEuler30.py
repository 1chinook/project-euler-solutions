numberList = set()

def digitFinder(number):
    return [int(d) for d in str(number)]



for i in range(2, 354295):
    digits = digitFinder(i)
    fives = [d**5 for d in digits]
    sumofAll = sum(fives)
    if(i == sumofAll):
        numberList.add(i)

print(sum(numberList))