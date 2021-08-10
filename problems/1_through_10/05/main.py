'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def merge(a, b):
    from collections import Counter
    na, nb = Counter(a), Counter(b)
    return list(Counter({k: max((na[k], nb[k])) for k in set(a + b)}).elements())

def product(list):
    result = 1
    for x in list:
        result *= x
    return result

def get_primes():
    import math
    yield 2
    previous_primes = [2]

    p = 3
    while True:
        max_check = math.ceil(math.sqrt(p))
        primes_to_check = [p % x == 0 for x in previous_primes if x <= max_check]

        if not any(primes_to_check):
            yield p
            previous_primes.append(p)

        p += 2

def get_prime_factors(number):
    factors = []
    
    for prime in get_primes():
        while number % prime == 0:
            number //= prime
            factors.append(prime)
        
        if number == 1:
            return factors

if __name__ == '__main__':
    factors_of_lcm = []
    for i in range(2, 21):
        factors_of_lcm = merge(factors_of_lcm, get_prime_factors(i))

    print(product(factors_of_lcm))