'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

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

if __name__ == '__main__':
    number = 600851475143
    for i, prime in enumerate(get_primes()):
        while number % prime == 0:
            number //= prime
        
        if number == 1:
            print(prime)
            break