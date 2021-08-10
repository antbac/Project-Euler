'''
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

def product(list):
    result = 1
    for x in list:
        result *= x
    return result

def merge(a, b):
    from collections import Counter
    na, nb = Counter(a), Counter(b)
    return list(Counter({k: max((na[k], nb[k])) for k in set(a + b)}).elements())

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

def approximate_reverse_arithmetic_sum(arithmetic_sum):
    import math
    return math.floor(math.sqrt(arithmetic_sum * 2))

def get_arithmetic_sum(i):
    return (i**2 + i) // 2

def get_number_of_divisors(number):
    prime_factors = get_prime_factors(number)
    
    result = 1
    for prime in set(prime_factors):
        result *= (prime_factors.count(prime) + 1)

    return result

if __name__ == '__main__':
    required_number_of_divisors = 500
    
    index = 1
    while index < 100:
        triangle_number = get_arithmetic_sum(index)

        # TODO: Use this algorithm once you understand it
        # https://www.geeksforgeeks.org/first-triangular-number-whose-number-of-divisors-exceeds-n/
        number_of_divisors = get_number_of_divisors(triangle_number)
        print(number_of_divisors)

        if number_of_divisors > required_number_of_divisors:
            print(triangle_number)
            break
        index += 1