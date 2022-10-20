"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    x = 2
    while len(list) < number_of_primes:
        if isPrime(x):
            list.append(x)
        x += 1
    return list

def isPrime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        return True
