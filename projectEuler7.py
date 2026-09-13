import math

def isPrime(number):
    origin = math.isqrt(number)
    for i in range(2, origin + 1):
        if number % i == 0:
            return False
    return True


count = 0
last_number = 0
i = 1

while count < 9999:
    for candidate in (6 * i - 1, 6 * i + 1):
        if isPrime(candidate):
            count += 1
            last_number = candidate
            if count == 9999:
                break
    i += 1

print(last_number) 