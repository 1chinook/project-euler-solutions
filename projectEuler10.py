import math

primes = set()

def isPrime(number):
    limit = int(math.sqrt(number)) + 1
    for i in range(3, limit, 2):
            if number % i == 0:
                return False
    return True
    
for i in range(3, 2000000, 2):
     if isPrime(i):
          primes.add(i)
    
print(sum(primes) + 2)