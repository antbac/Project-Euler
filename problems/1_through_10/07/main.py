'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
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
    prime_index = 10001
    for i, prime in enumerate(get_primes()):
        if i == prime_index - 1:
            print(prime)
            break