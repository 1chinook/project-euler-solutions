primes = set()

def isPrime(number):
    for i in range(2,int(number**0.5 + 1)):
        if number % i == 0:
            return False
    return True

def primeFinder(number):
    for i in range(2, int(number**0.5 + 1)):
        if number % i == 0:
            if isPrime(i):
                primes.add(i)

primeFinder(600851475143)
print(max(primes))
        
